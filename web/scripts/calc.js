//"use strict";

class calc {
    constructor() {
        this.inputs = [''];
        this.displayId = "calcDisplay";
        this.operator = '';
    }
    
    enterNum(entry) {
        //var inputNum = Number(entry);
        var last = this.inputs.length - 1;
        this.inputs[last] += String(entry);
        document.getElementById(this.displayId).innerHTML = this.inputs[last];
    }
    
    add() {
        console.log("Setting plus sign!");
        this.inputs.push('+');
        this.inputs.push('');
    }
    
    subtract() {
        console.log("Setting minus sign!");
        this.inputs.push('-');
        this.inputs.push('');
    }
    
    multiply() {
        console.log("Setting multiplication sign!");
        this.inputs.push('*');
        this.inputs.push('');
    }
    
    divide() {
        console.log("Setting division sign!");
        this.inputs.push('/');
        this.inputs.push('');
    }
    
    equals() {
        console.log("Equals functions has been called!");
        var last = this.inputs.length - 1;
        var total = Number(this.inputs[0]);
        for (var i = 1; i < last; i += 2) {
            console.log("Value of input: " + this.inputs[i]);
            if (this.inputs[i] === '+') {
                console.log("Plus sign detected!");
                total += Number(this.inputs[i + 1]);
            } else if (this.inputs[i] === '-') {
                console.log("Minus sign detected!")
                total -= Number(this.inputs[i + 1]);
            } else if (this.inputs[i] === '*') {
                console.log("Multiplication sign detected!")
                total *= Number(this.inputs[i + 1]);
            } else if (this.inputs[i] === '/') {
                console.log("Division sign detected!")
                total /= Number(this.inputs[i + 1]);
            }
        }
        document.getElementById(this.displayId).innerHTML = String(total);
        this.inputs = [String(total)];
    }
    
    clearScreen() {
        this.inputs = [''];
        document.getElementById(this.displayId).innerHTML = "";
    }
}

cl = new calc();

