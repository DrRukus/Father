#!/bin/ruby

load 'computer.rb'

computers = Hash.new
 
puts "Would you like to open a session? (y or n)"
choice = gets.chomp
if choice == "y"
    puts "Enter a username: "
    uname = gets.chomp
    pw = TRUE
    while pw
        puts "Enter a password: "
        pword = gets.chomp
        puts "Confirm password: "
        pwordConf = gets.chomp
        if pwordConf == pword
            computers[uname] = Computer.new(uname, pword)
            pw = FALSE
        else
            puts "Passwords did not match!  Re-enter? (y or no)"
            reEnter = gets.chomp
            if !(reEnter == "y")
                pw = FALSE
            else
                pw = TRUE
            end
        end
    end
else
    puts "Ok thanks, dick"
end

puts Computer.get_users
