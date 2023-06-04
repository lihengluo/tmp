from simple_test_Diana import check_binary
import pdb
import Diana
import circuit

def test_circuit():
    dur, ownerkey, keyleft, keyright = Diana.Setup()
    cb = check_binary(16)
    ca = check_binary(16)
    dur, ct1, ct2=Diana.Encrypt('1145rrrr5' , 1, '0')
    num1 = cb.insert(ct1)
    num2 = ca.insert(ct2)
    print(num1)
    print('x',num2)
    # decrypt
    
    
    
    
    print('------------------')
    
    b_new_list = circuit.save(num1, num2, circuit.b_list, circuit.b_order, circuit.b_input, 16)
    # b_new_list = circuit.save(0, 8, b_new_list, circuit.b_order, circuit.b_input, 16)

    res = circuit.run(circuit.readBit(), 4, b_new_list)
    # res = run(readBit(), 2, a_new_list)

    print(res)


if __name__ == '__main__':
    print("")
    test_circuit()