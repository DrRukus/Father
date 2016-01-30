#!/bin/ruby

puts "Give me a sentance: "
user_input = gets.chomp.downcase!
if user_input.include? "sh"
    user_input.gsub!(/sh/, "th")
    puts "New string is: #{user_input}"
elsif user_input.include? "s"
    user_input.gsub!(/s/, "th")
    puts "New string is: #{user_input}"
else
    puts "No \"s\'s\" detected, bitch!"
end
