#!/usr/bin/env ruby
require 'set'
set = Set.new
2.upto(100) {|a| 2.upto(100) {|b| set.add(a**b) }}
puts set.size
