//
//  ViewController.swift
//  Filterer
//
//  Created by Jack on 2015-09-22.
//  Copyright © 2015 UofT. All rights reserved.
//

import UIKit

class CustomCollectionCellView : UICollectionViewCell {
    
    @IBOutlet var previewImageView: UIImageView!
    @IBOutlet var filterNameLabel: UILabel!
}

class FilterMenuItem {
    let name: String?
    let imageName: String?
    let factory: () -> ImageFilter
    
    init(name: String?, imageName: String?, filterFactory: () -> ImageFilter) {
        self.name = name
        self.imageName = imageName
        self.factory = filterFactory
    }
}

class ViewController: UIViewController, UIImagePickerControllerDelegate,
    UINavigationControllerDelegate, UICollectionViewDataSource,
    UICollectionViewDelegate {

    let filters = [
        FilterMenuItem(name: "Sepia", imageName:  "sepia") { () -> ImageFilter in
            return SepiaFilter()
        },
        FilterMenuItem(name: "Brightness", imageName: "bright") { () -> ImageFilter in
            return BrightnessFilter()
        },
        FilterMenuItem(name: "Contrast", imageName: "contrast") { () -> ImageFilter in
            return ContrastFilter()
        },
        FilterMenuItem(name: "Gamma Correction", imageName: "gamma") { () -> ImageFilter in
            return GammaCorrectionFilter()
        },
        FilterMenuItem(name: "Grayscale", imageName: "gray") { () -> ImageFilter in
            return GrayScaleFilter()
        },
        FilterMenuItem(name: "Red", imageName: "red") { () -> ImageFilter in
            return RedFilter()
        },
        FilterMenuItem(name: "Green", imageName: "green") { () -> ImageFilter in
            return GreenFilter()
        },
        FilterMenuItem(name: "Blue", imageName: "blue") { () -> ImageFilter in
            return BlueFilter()
        },
        FilterMenuItem(name: "Yellow", imageName: "yellow") { () -> ImageFilter in
            return YellowFilter()
        },
        FilterMenuItem(name: "Purple", imageName: "purple") { () -> ImageFilter in
            return PurpleFilter()
        },
    ]
        
    var filteredImage: UIImage? {
        didSet {
            if filteredImage == nil {
                shareButton.enabled = false
                editButton.enabled = false
                compareButton.enabled = false
            } else {
                shareButton.enabled = true
                editButton.enabled = true
                compareButton.enabled = true
            }
        }
    }
    
    var currentFilter: ImageFilter?
    
    var originalImage: UIImage?
    
    @IBOutlet var filteredImageView: UIImageView!
    @IBOutlet var imageView: UIImageView!
    
    @IBOutlet var secondaryMenu: UIView!
    
    @IBOutlet var editFilterMenu: UIView!
    
    @IBOutlet var bottomMenu: UIView!
    
    @IBOutlet var filterButton: UIButton!
    
    @IBOutlet var originalLabel: UILabel!
    
    @IBOutlet var editButton: UIButton!
    
    @IBOutlet var compareButton: UIButton!
    
    @IBOutlet var shareButton: UIButton!
    
    @IBOutlet var filtersCollectionView: UICollectionView!
    
    @IBOutlet var editFilterSlider: UISlider!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        originalImage = imageView.image
        filteredImage = nil
        originalLabel.alpha = 0.0
        secondaryMenu.backgroundColor = UIColor.whiteColor().colorWithAlphaComponent(0.5)
        secondaryMenu.translatesAutoresizingMaskIntoConstraints = false
        editFilterMenu.backgroundColor = UIColor.whiteColor().colorWithAlphaComponent(0.5)
        editFilterMenu.translatesAutoresizingMaskIntoConstraints = false
        filtersCollectionView.dataSource = self
        filtersCollectionView.delegate = self
    }
    
    func collectionView(collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return section == 0 ? filters.count : 0
    }
    
    func collectionView(collectionView: UICollectionView, cellForItemAtIndexPath indexPath: NSIndexPath) -> UICollectionViewCell {
        let cell = filtersCollectionView.dequeueReusableCellWithReuseIdentifier("Filter Cell", forIndexPath: indexPath) as! CustomCollectionCellView
        let f = filters[indexPath.row]
        cell.filterNameLabel.text = f.name
        if let imageName = f.imageName {
            cell.previewImageView.image = UIImage(named: imageName)
        }
        return cell
    }
    
    func collectionView(collectionView: UICollectionView, didSelectItemAtIndexPath indexPath: NSIndexPath) {
        let f = filters[indexPath.row]
        currentFilter = f.factory()
        applyFilter()
    }

    func applyFilter() {
        if let filter = currentFilter {
            let src = RGBAImage(image: originalImage!)
            let dst = filter.filter(src!)
            showFilteredImage()
            filteredImage = dst.toUIImage()
            filteredImageView.image = filteredImage
        }
    }
    
    @IBAction func onEdit(sender: UIButton) {
        if (filterButton.selected) {
            hideSecondaryMenu()
            filterButton.selected = false
        }
        if (compareButton.selected) {
            showFilteredImage()
            compareButton.selected = false
        }
        
        if (sender.selected) {
            hideEditFilterMenu()
            sender.selected = false
        } else {
            showEditFilterMenu()
            sender.selected = true
        }
    }
    
    // MARK: Share
    @IBAction func onShare(sender: AnyObject) {
        let activityController = UIActivityViewController(activityItems: ["Check out our really cool app", filteredImage!], applicationActivities: nil)
        presentViewController(activityController, animated: true, completion: nil)
    }
    
    // MARK: New Photo
    @IBAction func onNewPhoto(sender: UIButton) {
        hideSecondaryMenu()
        hideEditFilterMenu()
        filterButton.selected = false
        editButton.selected = false
        
        let actionSheet = UIAlertController(title: "New Photo", message: nil, preferredStyle: .ActionSheet)
        
        actionSheet.addAction(UIAlertAction(title: "Camera", style: .Default, handler: { action in
            self.showCamera()
        }))
        
        actionSheet.addAction(UIAlertAction(title: "Album", style: .Default, handler: { action in
            self.showAlbum()
        }))
        
        actionSheet.addAction(UIAlertAction(title: "Cancel", style: .Cancel, handler: nil))
        
        if let popoverController = actionSheet.popoverPresentationController {
            popoverController.sourceView = sender
            popoverController.sourceRect = sender.bounds
        }
        self.presentViewController(actionSheet, animated: true, completion: nil)
    }
    
    func showCamera() {
        let cameraPicker = UIImagePickerController()
        cameraPicker.delegate = self
        cameraPicker.sourceType = .Camera
        
        presentViewController(cameraPicker, animated: true, completion: nil)
    }
    
    func showAlbum() {
        let cameraPicker = UIImagePickerController()
        cameraPicker.delegate = self
        cameraPicker.sourceType = .PhotoLibrary
        
        presentViewController(cameraPicker, animated: true, completion: nil)
    }
    
    // MARK: UIImagePickerControllerDelegate
    func imagePickerController(picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [String : AnyObject]) {
        dismissViewControllerAnimated(true, completion: nil)
        if let image = info[UIImagePickerControllerOriginalImage] as? UIImage {
            filteredImage = nil
            originalImage = createScaledImage(image)
            imageView.image = originalImage
            imageView.alpha = 1.0
            originalLabel.alpha = 0.0
        }
    }
    
    private func createScaledImage(image: UIImage) -> UIImage {
        let scaledSize = CGFloat(800)
        let landscape = image.size.width > image.size.height
        let ratio = CGFloat(image.size.width) / CGFloat(image.size.height)
        let newWidth = landscape ? scaledSize : scaledSize * ratio
        let newHeight = landscape ? scaledSize / ratio : scaledSize
        UIGraphicsBeginImageContext(CGSize(width: newWidth, height: newHeight))
        image.drawInRect(CGRectMake(0, 0, newWidth, newHeight))
        let outImage = UIGraphicsGetImageFromCurrentImageContext()
        UIGraphicsEndImageContext()
        return outImage
    }
    
    func imagePickerControllerDidCancel(picker: UIImagePickerController) {
        dismissViewControllerAnimated(true, completion: nil)
    }
    
    // MARK: Filter Menu
    @IBAction func onFilter(sender: UIButton) {
        if (editButton.selected) {
            hideEditFilterMenu()
            editButton.selected = false
        }
        if (compareButton.selected) {
            showFilteredImage()
            compareButton.selected = false
        }
        
        if (sender.selected) {
            hideSecondaryMenu()
            sender.selected = false
        } else {
            showSecondaryMenu()
            sender.selected = true
        }
    }
    
    func showSecondaryMenu() {
        if editButton.selected {
            editButton.selected = false
            hideEditFilterMenu()
        }
        view.addSubview(secondaryMenu)
        
        let bottomConstraint = secondaryMenu.bottomAnchor.constraintEqualToAnchor(bottomMenu.topAnchor)
        let leftConstraint = secondaryMenu.leftAnchor.constraintEqualToAnchor(view.leftAnchor)
        let rightConstraint = secondaryMenu.rightAnchor.constraintEqualToAnchor(view.rightAnchor)
        
        let heightConstraint = secondaryMenu.heightAnchor.constraintEqualToConstant(120)
        
        NSLayoutConstraint.activateConstraints([bottomConstraint, leftConstraint, rightConstraint, heightConstraint])
        
        view.layoutIfNeeded()
        
        self.secondaryMenu.alpha = 0
        UIView.animateWithDuration(0.4) {
            self.secondaryMenu.alpha = 1.0
        }
    }

    func hideSecondaryMenu() {
        UIView.animateWithDuration(0.4, animations: {
            self.secondaryMenu.alpha = 0
            }) { completed in
                if completed == true {
                    self.secondaryMenu.removeFromSuperview()
                }
        }
    }

    func showEditFilterMenu() {
        if filterButton.selected {
            filterButton.selected = false
            hideSecondaryMenu()
        }
        
        view.addSubview(editFilterMenu)
        
        if let value = currentFilter?.value {
            editFilterSlider.value = Float(value)
        }
        
        let bottomConstraint = editFilterMenu.bottomAnchor.constraintEqualToAnchor(bottomMenu.topAnchor)
        let leftConstraint = editFilterMenu.leftAnchor.constraintEqualToAnchor(view.leftAnchor)
        let rightConstraint = editFilterMenu.rightAnchor.constraintEqualToAnchor(view.rightAnchor)
        
        let heightConstraint = editFilterMenu.heightAnchor.constraintEqualToConstant(44)
        
        NSLayoutConstraint.activateConstraints([bottomConstraint, leftConstraint, rightConstraint, heightConstraint])
        
        view.layoutIfNeeded()
        
        self.editFilterMenu.alpha = 0
        UIView.animateWithDuration(0.4) {
            self.editFilterMenu.alpha = 1.0
        }
    }
    
    func hideEditFilterMenu() {
        UIView.animateWithDuration(0.4, animations: {
            self.editFilterMenu.alpha = 0
            }) { completed in
                if completed == true {
                    self.editFilterMenu.removeFromSuperview()
                }
        }
    }

    @IBAction func onFilterValueChanged(sender: UISlider) {
        if var filter = currentFilter {
            filter.value = Double(sender.value)
            applyFilter()
        }
    }
    
    func showFilteredImage() {
        UIView.animateWithDuration(0.3) {
            self.imageView.alpha = 0.0
            self.originalLabel.alpha = 0.0
        }
    }
    
    func showOriginalImage() {
        UIView.animateWithDuration(0.3) {
            self.imageView.alpha = 1.0
            self.originalLabel.alpha = 1.0
        }
    }
    
    @IBAction func onCompare(sender: UIButton) {
        if (filterButton.selected) {
            hideSecondaryMenu()
            filterButton.selected = false
        }
        if (editButton.selected) {
            hideEditFilterMenu()
            editButton.selected = false
        }
        
        if sender.selected {
            showFilteredImage()
            sender.selected = false
        } else {
            showOriginalImage()
            sender.selected = true
        }
    }
    
    @IBAction func onImagePressed(sender: UIButton) {
        if let _ = compareButton.selected ? nil : filteredImage {
            showOriginalImage()
        }
    }
    
    
    @IBAction func onImageReleased(sender: UIButton) {
        if let _ = compareButton.selected ? nil : filteredImage {
            showFilteredImage()
        }
    }
}

