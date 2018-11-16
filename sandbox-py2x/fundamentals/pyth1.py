# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "scott_r_parker"
__date__ = "$Jul 10, 2017 4:41:45 PM$"

if __name__ == "__main__":
	print ("Output Formatting Testing")
	print ('{0} :spacer: {1}'.format('replace {0} left justify', 'replace{1} left justify'))
	print ("Now sticking in a for-loop to do something with formatting...")
	for x in range (0, 15):
		print ('line {0} :spacer:  10^{0}={1}'.format(x, 10**x))
		
	print ('{0:>16} :spacer: {1:>28}'.format('rep{0}:right:16', 'rep{1}:28chrs:right just'))
	for x in range (0, 15):
		print ('{0:>5} :spacer: 10^{0:>2}={1:>18}'.format(x, 10**x))
		
	for x in range (0, 111):
		print ('{0:<6} {2:<4}{1} {2:>4}*{2:<4}{3:>17}'.format('Line:', ':spacer:', x, x*x))
		
		