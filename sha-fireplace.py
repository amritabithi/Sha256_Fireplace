#                                                                       #
#   Amrita Bithi 2024 - https://github.com/amritabithi/Sha_Fireplace/   #
#                                                                       #

from colorama import Fore;
from hashlib import sha256;

def main():
	hasher = sha256();
	hash_message = 0;
	prev_message = 0;
	i = 0;
	while True:
		i += 1;
		hash_message = int(hasher.hexdigest(),16);
		hash_message ^= prev_message;
		hash_message |= int(sha256(bin(hash_message)[42:].encode()).hexdigest(),16);
		hash_message &= hash_message;
		prev_message = hash_message;
		hasher = sha256(hex(hash_message).encode());
		output = bin( int(hasher.hexdigest(),16) )[2:];
		output = output[1:170].replace("0",Fore.BLACK+" "+Fore.RESET).replace("1",Fore.RED+"▓"+Fore.RESET);
		ext = Fore.RED+"▓"+Fore.RESET+Fore.RED+"▓"+Fore.RESET+Fore.RED+"▓"+Fore.RESET;
		output = output.replace(ext,Fore.RED+"▓"+Fore.LIGHTRED_EX+"▓"+Fore.RED+"▓"+Fore.RESET);
		if i % (78*32) == 0:
			print(output);
main();
