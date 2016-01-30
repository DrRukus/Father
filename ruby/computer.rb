#!/bin/ruby

class Computer
    @@users = Hash.new
    def initialize(username=nil, password=nil)
        @username = username
        @password = password
        @files = Hash.new
        @@users[username] = password
    end

    def authenticate
        puts "Enter password: "
        pword = gets.chomp
        if pword == @password
            return TRUE
        else
            return FALSE
       end
    end

    def createFile(filename)
        if authenticate
            if @files.has_key?(filename)
                puts "\nFile has already been created\n"
                puts "Filename: #{filename}"
                puts "Time created: #{@files[filename]}"
         	puts "Do you want to replace it? (y or n)"
                replace = gets.chomp
                if replace == "y"
                    self.deleteFile(filename)
                else
                    return
                end
            end
        else
            puts "Incorrect password.  Prepare for termination"
            puts "Have a nice day"
        end
        time = Time.now
        @files[filename] = time
        puts "\n#{filename} was created at #{time} by #{@username}, dawg!\n"
    end

    def deleteFile(filename)
        if @files.has_key?(filename)
            @files.delete(filename)
        else
            puts "\nError: No such file.\n"
        end
    end
    
    def Computer.get_users
        return @@users
    end

    def printUser
        puts "\nCurrent Session:"
        puts "========================="
        puts "Username: #{@username}\n"
    end

    def printFiles
        puts "\nList of Files"
        puts "========================"
        @files.each { |k, v| puts "Filename: #{k}\n Time Created: #{v}\n" }
    end
end

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
