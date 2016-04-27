//
//  ImageFilterer.swift
//  Filterer
//
//  Created by Stefano Pacifici on 27/12/15.
//  Copyright © 2015 UofT. All rights reserved.
//

import Foundation

public typealias Pixels = UnsafeMutableBufferPointer<Pixel>

protocol ImageFilter {
    func getValue() -> Double
    func setValue(newValue: Double)

    func applyFilter(src: Pixels, dst: Pixels, w: Int, h: Int, x: Int, y: Int)
}

extension ImageFilter {
    var value: Double {
        get {
            return getValue()
        }
        set(newValue) {
            setValue(newValue)
        }
    }
    func filter(image: RGBAImage) -> RGBAImage {
        let width = image.width
        let height = image.height
        let outImage = RGBAImage(width: width, height: height)!
        let inPixels: Pixels = image.pixels
        let outPixels: Pixels = outImage.pixels
        for row in 0...height - 1 {
            for col in 0...width - 1 {
                applyFilter(inPixels, dst: outPixels, w: width, h: height, x: col, y: row)
            }
        }
        return outImage
    }

    func normalize(value: Int) -> UInt8 {
        return UInt8(min(255, max(0, value)))
    }
}

public class IdentityFilter: ImageFilter {
    var v: Double = 0.0
    
    func getValue() -> Double {
        return v
    }
    
    func setValue(newValue: Double) {
        v = min(1.0, max(-1.0, newValue))
    }
    
    public func applyFilter(src: Pixels, dst: Pixels, w: Int, h: Int, x: Int, y: Int) {
        let index = x + w * y
        dst[index] = applyPixel(src[index])
    }
    
    func applyPixel(src: Pixel) -> Pixel {
        return src
    }
}

public class ConvolutionFilter: IdentityFilter {
    private var matrix: [Int]
    private var size: Int
    private var halfSize: Int
    
    override init() {
        matrix = []
        size = 0
        halfSize = 0
        super.init()
        setValue(0.0)
    }
    
    override func setValue(newValue: Double) {
        super.setValue(newValue)
        self.matrix = createMatrix(v)
        self.size = Int(sqrt(Double(matrix.count))+0.5)
        self.halfSize = self.size / 2
    }
    
    func createMatrix(v: Double) -> [Int] {
        preconditionFailure("Must be overridden")
    }
    
    override public func applyFilter(src: Pixels, dst: Pixels, w: Int, h: Int, x: Int, y: Int) {
        let imageSize = w * h
        var accRed = 0
        var accGreen = 0
        var accBlue = 0
        var acc = 0
        for dy in -halfSize...halfSize {
            let yOffset = (y + dy) * w
            let cmYOffset = (halfSize + dy) * size
            for dx in -halfSize...halfSize {
                let cmIndex = (halfSize + dx) + cmYOffset
                let c = matrix[cmIndex]
                let pIndex = (x + dx) + yOffset
                if (c != 0 && pIndex >= 0 && pIndex < imageSize) {
                    let pixel = src[pIndex]
                    acc = acc + c
                    accRed = accRed + Int(pixel.red) * c
                    accGreen = accGreen + Int(pixel.green) * c
                    accBlue = accBlue + Int(pixel.blue) * c
                }
            }
        }
        let index = x + y * w
        var pixel = dst[index]
        pixel.alpha = 255
        pixel.red = normalize(accRed / acc)
        pixel.green = normalize(accGreen / acc)
        pixel.blue = normalize(accBlue / acc)
        dst[index] = pixel
    }
}

public class MultiplyFilter: IdentityFilter {
    private let matrix: [Double]
    private var m = 1.0
    
    init(matrix: [Double]) {
        self.matrix = matrix
        super.init()
        self.setValue(1.0)
    }
    
    override func setValue(newValue: Double) {
        super.setValue(newValue)
        m = (1.0 + newValue) / 2.0
    }
    
    override func applyPixel(src: Pixel) -> Pixel {
        var out = Pixel(value: 0xffffffff)
        let r = Double(src.red)
        let g = Double(src.green)
        let b = Double(src.blue)
        out.red = normalize(Int((r * matrix[0] + g * matrix[1] + b * matrix[2]) * m))
        out.green = normalize(Int((r * matrix[3] + g * matrix[4] + b * matrix[5]) * m))
        out.blue = normalize(Int((r * matrix[6] + g * matrix[7] + b * matrix[8]) * m))
        return out
    }
}

public class AddFilter: IdentityFilter {
    private let dr, dg, db: Int;
    
    init(dr: Int, dg: Int, db: Int) {
        self.dr = dr
        self.dg = dg
        self.db = db
    }
    
    override func applyPixel(src: Pixel) -> Pixel {
        var out = Pixel(value: 0xffffffff)
        let r = Int(src.red)
        let g = Int(src.green)
        let b = Int(src.blue)
        out.red = normalize(r + dr)
        out.green = normalize(g + dg)
        out.blue = normalize(b + db)
        return out
    }
}

public class RedFilter: MultiplyFilter {
    init() {
        super.init(matrix: [
            1.0, 0.0, 0.0,
            0.0, 0.0, 0.0,
            0.0, 0.0, 0.0])
    }
}

public class GreenFilter: MultiplyFilter {
    init() {
        super.init(matrix: [
            0.0, 0.0, 0.0,
            0.0, 1.0, 0.0,
            0.0, 0.0, 0.0])
    }
}

public class BlueFilter: MultiplyFilter {
    init() {
        super.init(matrix: [
            0.0, 0.0, 0.0,
            0.0, 0.0, 0.0,
            0.0, 0.0, 1.0])
    }
}

public class YellowFilter: IdentityFilter {
    
    private let mul: MultiplyFilter
    private let add: AddFilter
    
    override func setValue(newValue: Double) {
        super.setValue(newValue)
        mul.setValue(newValue)
    }
    
    override init() {
        self.add = AddFilter(dr: 1000, dg:1000, db: 0)
        self.mul = MultiplyFilter(matrix: [
            0.5, 0.0, 0.5,
            0.0, 0.5, 0.5,
            0.0, 0.0, 1.0])
        super.init()
        self.setValue(1.0)
    }
    
    override func applyPixel(src: Pixel) -> Pixel {
        return mul.applyPixel(add.applyPixel(src))
    }
}

public class PurpleFilter: IdentityFilter {
    
    private let mul: MultiplyFilter
    private let add: AddFilter

    override func setValue(newValue: Double) {
        super.setValue(newValue)
        mul.setValue(newValue)
    }

    override init() {
        self.add = AddFilter(dr: 1000, dg:0, db: 1000)
        self.mul = MultiplyFilter(matrix: [
            0.5, 0.5, 0.0,
            0.0, 1.0, 0.0,
            0.0, 0.5, 0.5])
        super.init()
        self.setValue(1.0)
    }
    
    override func applyPixel(src: Pixel) -> Pixel {
        return mul.applyPixel(add.applyPixel(src))
    }
}

public class ContrastFilter: IdentityFilter {
    private var factor = 0.0
    
    override init() {
        super.init()
        setValue(0.0)
    }
    
    override public func setValue(newValue: Double) {
        super.setValue(newValue)
        let contrast = (1.0 + newValue) / 2.0 * 255.0
        factor = (259.0 * (contrast + 255.0)) / (255.0 * (259.0 - contrast))
    }
    
    override public func applyFilter(src: Pixels, dst: Pixels, w: Int, h: Int, x: Int, y: Int) {
        let index = x + y * w
        var pixel = src[index]
        let red = factor * (Double(pixel.red) - 128.0) + 128.0
        let green = factor * (Double(pixel.green) - 128.0) + 128.0
        let blue = factor * (Double(pixel.blue) - 128.0) + 128.0
        pixel.alpha = 255
        pixel.red = normalize(Int(red))
        pixel.green = normalize(Int(green))
        pixel.blue = normalize(Int(blue))
        dst[index] = pixel
    }
}

public class BrightnessFilter: IdentityFilter {
    private var f = 0.0
    
    override public func setValue(newValue: Double) {
        super.setValue(newValue)
        f = v * 255.0
    }
    
    override public func applyFilter(src: Pixels, dst: Pixels, w: Int, h: Int, x: Int, y: Int) {
        let index = x + y * w
        var pixel = src[index]
        let red = Double(pixel.red) + f
        let green = Double(pixel.green) + f
        let blue = Double(pixel.blue) + f
        pixel.alpha = 255
        pixel.red = normalize(Int(red))
        pixel.green = normalize(Int(green))
        pixel.blue = normalize(Int(blue))
        dst[index] = pixel
    }
}

public class GammaCorrectionFilter: IdentityFilter {
    private var gc = 9.0 / 32.0 // default value
    
    override public func setValue(newValue: Double) {
        super.setValue(newValue)
        let gamma = 3.99 * v + 4.0 // 0.01 to 7.99
        gc = 1.0 / gamma
    }
    
    override init() {
        super.init()
        self.setValue(0.0)
    }
    
    override public func applyFilter(src: Pixels, dst: Pixels, w: Int, h: Int, x: Int, y: Int) {
        let index = x + y * w
        var pixel = src[index]
        let red = 255.0 * pow(Double(pixel.red) / 255.0, gc)
        let green = 255.0 * pow(Double(pixel.green) / 255.0, gc)
        let blue = 255.0 * pow(Double(pixel.blue) / 255.0, gc)
        pixel.alpha = 255
        pixel.red = normalize(Int(red))
        pixel.green = normalize(Int(green))
        pixel.blue = normalize(Int(blue))
        dst[index] = pixel
    }
}

public class SolarizeFilter: IdentityFilter {
    private var threshold: UInt8 = 127
    
    override public func setValue(newValue: Double) {
        super.setValue(newValue)
        threshold = normalize(Int(127.6 * v + 127.5))
    }
    
    override public func applyFilter(src: Pixels, dst: Pixels, w: Int, h: Int, x: Int, y: Int) {
        let index = x + y * w
        var pixel = src[index]
        let red = pixel.red < threshold ? 255 - pixel.red : pixel.red
        let green = pixel.green < threshold ? 255 - pixel.green : pixel.green
        let blue = pixel.blue < threshold ? 255 - pixel.blue : pixel.blue
        pixel.alpha = 255
        pixel.red = normalize(Int(red))
        pixel.green = normalize(Int(green))
        pixel.blue = normalize(Int(blue))
        dst[index] = pixel
    }
}

public class SepiaFilter: MultiplyFilter {
    init() {
        super.init(matrix: [
            0.393, 0.769, 0.189,
            0.349, 0.686, 0.168,
            0.272, 0.534, 0.131])
    }
}

public class GrayScaleFilter: MultiplyFilter {
    init() {
        super.init(matrix: [
            0.299, 0.587, 0.114,
            0.299, 0.587, 0.114,
            0.299, 0.587, 0.114])
    }
}

public class BlurFilter: ConvolutionFilter {
    override func createMatrix(v: Double) -> [Int] {
        let size = 11 + Int(v * 8.0)
        let hs = size / 2
        let v = hs + 1
        var row: [Int] = []
        for i in -hs...hs {
            row.append(v - abs(i))
        }
        var matrix: [Int] = []
        for i in -hs...hs {
            let d = abs(i) + 1
            for j in 0...row.count-1 {
                matrix.append(row[j] / d)
            }
        }
        return matrix
    }
}

public class TestFilter: ConvolutionFilter {
    override func createMatrix(v: Double) -> [Int] {
        return [
            0, -2 ,0,
            3, 0, -2,
            0, 3, 0
        ]
    }
}
