import p1
import p2
import p3

p = int(input("Enter p: "))
q = int(input("Enter q: "))
e = int(input("Enter e: "))
u_number = p3.get_u_number()

print("------------------P1------------------")

n = p * q
print("n: ", n)

phi_of_n = p1.phi(n)
print(f"\u03c6(n): {phi_of_n}")

d = p1.find_inverse_e(e=e, divisor=phi_of_n)

print("d: ", d)

print("------------------P2------------------")

phi_of_phi_of_n = p1.phi(phi_of_n)

print(f"\u03c6(\u03c6(n)): {phi_of_phi_of_n}")

val1 = phi_of_phi_of_n - 1

print(f"\u03c6(\u03c6(n)) - 1: {val1}")

exponent_in_binary = p2.convert_to_binary(val1)

p2.print_powers_of_two(exponent_in_binary=exponent_in_binary)

mod_powers_of_two = p2.calculate_mod_e_powers_of_two(e=e, max_power_of_two=len(exponent_in_binary), divisor=phi_of_n)

product_modulo_n = p2.calculate_mod_from_powers_of_two(arr=mod_powers_of_two, divisor=phi_of_n, binary_exponent=exponent_in_binary)

print("Product modulo n: ", product_modulo_n)

p2.print_powers_mod(arr=mod_powers_of_two, binary_exponent=exponent_in_binary)

if product_modulo_n != d:
    raise Exception("Program is producing wrong output. Restart it or do work by hand")

print("------------------P3------------------")

x_list = p3.calculate_x_list(u_number=u_number)

decrypted_list = p3.calculate_decrypted_list(x_list=x_list, d=d, divisor=n)

re_encrypted_u_number = p3.encrypt_u_number(decrypted_arr=decrypted_list, e=e, divisor=n)

if re_encrypted_u_number != u_number:
    raise Exception("Program is producing wrong output. Restart it or do work by hand")

p3.print_u_number_table(u_number=u_number, x_list=x_list, list_decrypted=decrypted_list)

