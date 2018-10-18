//
//  ViewController.swift
//  Magic 8 Ball
//
//  Created by Daniel Schmidt on 9/30/18.
//  Copyright © 2018 Getoryx. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    let ballArray = ["ball1", "ball2", "ball3", "ball4", "ball5"]
    var randomBallNumber: Int = 0

    @IBOutlet weak var imageView: UIImageView!
    
    func updateImageView() {
        randomBallNumber = Int.random(in: 0 ... 4)
        imageView.image = UIImage(named: ballArray[randomBallNumber])
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        updateImageView()
        
    }

    @IBAction func askButtonPressed(_ sender: Any) {
        
        updateImageView()
        
    }
    
    override func motionEnded(_ motion: UIEvent.EventSubtype, with event: UIEvent?) {
        
        updateImageView()
        
    }
    
}

