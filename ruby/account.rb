class Account
    def initialize(name, balance=100)
        @name = name
        @balance = balance
    end
    
    attr_reader :name, :balance
    
    public
    def display_balance(pin_number)
        if pin_number == pin
            puts "Balance: $#{@balance}"
        else
            puts pin_error
        end
    end
    
    public
    def withdraw(pin_number, amount)
        if pin_number == pin
            @balance -= amount
            puts "Withdrew #{amount}. New balance: $#{@balance}."
        else
            puts pin_error
        end
    end
    
    private
    def pin
        @pin = 1234
    end
    
    private
    def pin_error
        "Access denied: incorrect PIN."
    end
end

checking_account = Account.new("Spongebob", 100)
