// Fizzbuzz activity 
// CS 6704 Spring 2024 
//
// Jeffrey Smith 01.23.2024
//

#include <iostream>

int main(){
	for(int i=0; i<20; i++) {
		if(i%3==0 &&  i%5==0) {
			std::cout << ("FizzBuzz") << std::endl;
		} else if(i%3==0) {
			std::cout << ("Fizz") << std::endl;
		} else if(i%5==0) {
			std::cout << ("Buzz") << std::endl;
		}
	}
	return 0;
}
