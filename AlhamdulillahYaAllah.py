#Pembagian 
tape1_divide = ['0', '0', '0', '0','0', '0', '0', '0','0', '1', '0', '0', '0', '1','B', 'B', 'B', 'B', 'B']
tape2_divide = ['B','B', 'B', 'B', 'B','B','B', 'B', 'B', 'B','B','B', 'B', 'B', 'B' ]
head1 = 0
head2 = 0
state = 0
accepting_state = 8 # State akhir untuk menghentikan mesin Turing

# Fungsi untuk mengubah tape dan posisi kepala
def action(write1, write2, move1, move2, next_state):
    global head1, head2, head3, state
    tape1_divide[head1] = write1
    tape2_divide[head2] = write2
    if move1 == 'R':
        head1 += 1
    elif move1 == 'L':
        head1 -= 1
    if move2 == 'R':
        head2 += 1
    elif move2 == 'L':
        head2 -= 1
    state = next_state

# Fungsi untuk menjalankan mesin Turing
def divide():
    global state
    if state == 0:
        if tape1_divide[head1] == '0' and tape2_divide[head2] == 'B':
            action('B', 'B', 'R', 'S',  1)
        elif tape1_divide[head1] == '1' and tape2_divide[head2] == 'B':
            action('1', 'B', 'R', 'S', accepting_state)
    elif state == 1:
        if tape1_divide[head1] == '0' and tape2_divide[head2] == 'B':
            action('0', 'B', 'R', 'S', 1)
        elif tape1_divide[head1] == '1' and tape2_divide[head2] == 'B':
            action('1', 'B', 'R', 'S', 2)
    elif state == 2:
        if tape1_divide[head1] == '0' and tape2_divide[head2] == 'B':
            action('0', 'B', 'R', 'S', 2)
        elif tape1_divide[head1] == 'X' and tape2_divide[head2] == 'B':
            action('X', 'B', 'R', 'S', 2)
        elif tape1_divide[head1] == '1' and tape2_divide[head2] == 'B':
            action('1', 'B', 'L', 'S', 3)
    elif state == 3:
        if tape1_divide[head1] == 'X' and tape2_divide[head2] == 'B':
            action('X', 'B', 'L', 'S', 3)
        elif tape1_divide[head1] == '0' and tape2_divide[head2] == 'B':
            action('X', 'B', 'L', 'S', 4)
    elif state == 4:
        if tape1_divide[head1] == '0' and tape2_divide[head2] == 'B':
            action('0', 'B', 'L', 'S', 5)
        elif tape1_divide[head1] == '1' and tape2_divide[head2] == 'B':
            action('1', 'B', 'R', 'S', 6)
    elif state == 5:
        if tape1_divide[head1] == '0' and tape2_divide[head2] == 'B':
            action('0', 'B', 'L', 'S', 5)
        elif tape1_divide[head1] == '1' and tape2_divide[head2] == 'B':
            action('1', 'B', 'L', 'S', 5)
        elif tape1_divide[head1] == 'B' and tape2_divide[head2] == 'B':
            action('B', 'B', 'R', 'S', 0)
    elif state == 6:
        if tape1_divide[head1] == '0' and tape2_divide[head2] == 'B':
            action('0', 'B', 'L', 'S', 6)
        elif tape1_divide[head1] == 'X' and tape2_divide[head2] == 'B':
            action('0', 'B', 'R', 'S', 6)
        elif tape1_divide[head1] == '1' and tape2_divide[head2] == 'B':
            action('1', '0', 'L', 'R', 7)
    elif state == 7:
        if tape1_divide[head1] == '0' and tape2_divide[head2] == 'B':
            action('0', 'B', 'L', 'S', 7)
        elif tape1_divide[head1] == '1' and tape2_divide[head2] == 'B':
            action('1', 'B', 'L', 'S', 7)
        elif tape1_divide[head1] == 'B' and tape2_divide[head2] == 'B':
            action('B', 'B', 'R', 'S', 0)


# Program utama untuk menjalankan mesin Turing sampai mencapai state accepting_state
while state != accepting_state:
    divide()

#Menghilangkan Blank berlebih pada tape 2
final_tape2_divide = ''.join(tape2_divide).rstrip('B')

# Output hasil akhir
print("===========HASIL PEMBAGIAN============")
print("Final tape1:",''.join(tape1_divide))
print("Final tape2:", final_tape2_divide)
print("Final state:", state)
print("Head1 position:", head1)
print("Head2 position:", head2)


# Inisialisasi tape dan posisi kepala dibaca log2(8)
tape1_log = [ '1', '0', '0', '1', 'B', 'B', 'B', 'B', 'B','B', 'B', 'B', 'B', 'B']
tape2_log = ['B', 'B', 'B', 'B']
head1 = 0
head2 = 0
state = 1
accepting_state = 13

# Fungsi untuk mengubah tape dan posisi kepala
def action(write1, write2, move1, move2, next_state):
    global head1, head2, state
    tape1_log[head1] = write1
    tape2_log[head2] = write2
    if move1 == 'R':
        head1 += 1
    elif move1 == 'L':
        head1 -= 1
    if move2 == 'R':
        head2 += 1
    elif move2 == 'L':
        head2 -= 1
    state = next_state

# Fungsi untuk menjalankan mesin Turing
def binary_logarithm():
    global state
    if state == 1:
        if tape1_log[head1] == '0' and tape2_log[head2] == 'B':
            action('B', 'B', 'R', 'S', 2)
        elif tape1_log[head1] == '1' and tape2_log[head2] == 'B':
            action('1', 'B', 'R', 'S', 9)
    elif state == 2:
        if tape1_log[head1] == '0' and tape2_log[head2] == 'B':
            action('0', 'B', 'R', 'S', 2)
        elif tape1_log[head1] == '1' and tape2_log[head2] == 'B':
            action('1', 'B', 'R', 'S', 3)
    elif state == 3:
        if tape1_log[head1] == '0' and tape2_log[head2] == 'B':
            action('0', 'B', 'R', 'S', 3)
        elif tape1_log[head1] == 'X' and tape2_log[head2] == 'B':
            action('X', 'B', 'R', 'S', 3)
        elif tape1_log[head1] == '1' and tape2_log[head2] == 'B':
            action('1', 'B', 'L', 'S', 4)
    elif state == 4:
        if tape1_log[head1] == 'X' and tape2_log[head2] == 'B':
            action('X', 'B', 'L', 'S', 4)
        elif tape1_log[head1] == '0' and tape2_log[head2] == 'B':
            action('X', 'B', 'L', 'S', 5)
    elif state == 5:
        if tape1_log[head1] == '0' and tape2_log[head2] == 'B':
            action('0', 'B', 'L', 'S', 6)
        elif tape1_log[head1] == '1' and tape2_log[head2] == 'B':
            action('1', 'B', 'R', 'S', 7)
    elif state == 6:
        if tape1_log[head1] == '0' and tape2_log[head2] == 'B':
            action('0', 'B', 'L', 'S', 6)
        elif tape1_log[head1] == '1' and tape2_log[head2] == 'B':
            action('1', 'B', 'L', 'S', 6)
        elif tape1_log[head1] == 'B' and tape2_log[head2] == 'B':
            action('B', 'B', 'R', 'S', 1)
    elif state == 7:
        if tape1_log[head1] == '0' and tape2_log[head2] == 'B':
            action('0', 'B', 'R', 'S', 7)
        elif tape1_log[head1] == '1' and tape2_log[head2] == 'B':
            action('1', 'B', 'R', 'S', 7)
        elif tape1_log[head1] == 'X' and tape2_log[head2] == 'B':
            action('0', 'B', 'R', 'S', 7)
        elif tape1_log[head1] == 'B' and tape2_log[head2] == 'B':
            action('0', 'B', 'L', 'S', 8)
    elif state == 8:
        if tape1_log[head1] == '0' and tape2_log[head2] == 'B':
            action('0', 'B', 'L', 'S', 8)
        elif tape1_log[head1] == '1' and tape2_log[head2] == 'B':
            action('1', 'B', 'L', 'S', 8)
        elif tape1_log[head1] == 'B' and tape2_log[head2] == 'B':
            action('B', 'B', 'R', 'S', 1)
    elif state == 9:
        if tape1_log[head1] == '0' and tape2_log[head2] == 'B':
            action('0', 'B', 'R', 'S', 9)
        elif tape1_log[head1] == '1' and tape2_log[head2] == 'B':
            action('1', 'B', 'R', 'S', 9)
        elif tape1_log[head1] == 'B' and tape2_log[head2] == 'B':
            action('B', 'B', 'L', 'S', 10)
        elif tape1_log[head1] == 'X' and tape2_log[head2] == 'B':
            action('B', 'B', 'R', 'S', accepting_state)
    elif state == 10:
        if tape1_log[head1] == '0' and tape2_log[head2] == 'B':
            action('B', 'B', 'L', 'S', 11)
        elif tape1_log[head1] == '1' and tape2_log[head2] == 'B':
            action('1', '0', 'L', 'R', 12)
    elif state == 11:
        if tape1_log[head1] == '0' and tape2_log[head2] == 'B':
            action('0', 'B', 'L', 'S', 11)
        elif tape1_log[head1] == '1' and tape2_log[head2] == 'B':
            action('1', 'B', 'L', 'S', 11)
        elif tape1_log[head1] == 'B' and tape2_log[head2] == 'B':
            action('0', 'B', 'R', 'S', 9)
    elif state == 12:
        if tape1_log[head1] == '0' and tape2_log[head2] == 'B':
            action('0', 'B', 'L', 'S', 12)
        elif tape1_log[head1] == '1' and tape2_log[head2] == 'B':
            action('1', 'B', 'L', 'S', 12)
        elif tape1_log[head1] == 'B' and tape2_log[head2] == 'B':
            action('B', 'B', 'R', 'S', 1)

# Program utama untuk menjalankan mesin Turing sampai mencapai state accepting_state
while state != accepting_state:
    binary_logarithm()

#Menghilangkan Blank berlebih pada tape 2
final_tape2_log = ''.join(tape2_log).rstrip('B')

# Output hasil akhir
print("\n==========HASIL LOGARITMA============")
print("Final tape1_log:", ''.join(tape1_log))
print("Final tape2_log:", final_tape2_log)
print("Final state:", state)


#Perkalian
# Inisialisasi tape dan posisi kepala
tape1 =  list(final_tape2_divide) + ['1'] + list(final_tape2_log) + ['1', 'B', 'B', 'B']
tape2 = ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B','B', 'B']
head1 = 0
head2 = 0
state = 0
accepting_state = 5 # State akhir untuk menghentikan mesin Turing

# Fungsi untuk mengubah tape dan posisi kepala
def action(write1, write2, move1, move2, next_state):
    global head1, head2, head3, state
    tape1[head1] = write1
    tape2[head2] = write2
    if move1 == 'R':
        head1 += 1
    elif move1 == 'L':
        head1 -= 1
    if move2 == 'R':
        head2 += 1
    elif move2 == 'L':
        head2 -= 1
    state = next_state

# Fungsi untuk menjalankan mesin Turing
def multiple():
    global state
    if state == 0:
        if tape1[head1] == '0' and tape2[head2] == 'B':
            action('0', 'B', 'R', 'S',  0)
        elif tape1[head1] == '1' and tape2[head2] == 'B':
            action('1', 'B', 'R', 'S', 1)
        elif tape1[head1] == 'B' and tape2[head2] == 'B':
            action('0', 'B', 'R', 'S', 0)
    elif state == 1:
        if tape1[head1] == '0' and tape2[head2] == 'B':
            action('0', 'B', 'R', 'S', 1)
        elif tape1[head1] == '1' and tape2[head2] == 'B':
            action('1', 'B', 'L', 'S', 2)
        elif tape1[head1] == 'X' and tape2[head2] == 'B':
            action('X', 'B', 'R', 'S', 1)
    elif state == 2:
        if tape1[head1] == '0' and tape2[head2] == 'B':
            action('X', 'B', 'L', 'S', 3)
        elif tape1[head1] == 'X' and tape2[head2] == 'B':
            action('X', 'B', 'L', 'S', 2)
        elif tape1[head1] == '1' and tape2[head2] == 'B':
            action('1', 'B', 'R', 'S', accepting_state)
    elif state == 3:
        if tape1[head1] == '0' and tape2[head2] == 'B':
            action('0', 'B', 'L', 'S', 3)
        elif tape1[head1] == '1' and tape2[head2] == 'B':
            action('1', 'B', 'L', 'S', 4)
    elif state == 4:
        if tape1[head1] == '0' and tape2[head2] == 'B':
            action('B', '0', 'L', 'R', 4)
        elif tape1[head1] == 'B' and tape2[head2] == 'B':
            action('B', 'B', 'R', 'S', 0)


# Program utama untuk menjalankan mesin Turing sampai mencapai state accepting_state
while state != accepting_state:
    multiple()

final_tape2_multiple = ''.join(tape2).rstrip('B')

# Output hasil akhir
print("\n==========HASIL PERHITUNGAN AKHIR============")
print("Final tape1:",''.join(tape1))
print("Final tape2:",final_tape2_multiple)
print("Final state:", state)
print("Head1 position:", head1)
print("Head2 position:", head2)
