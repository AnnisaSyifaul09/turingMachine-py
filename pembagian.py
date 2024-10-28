# Inisialisasi tape dan posisi kepala
tape1 = ['0', '0', '0', '0','1', '0', '0','0', '0', '1','B', 'B', 'B', 'B', 'B']
tape2 = ['B', 'B', 'B', 'B', 'B', 'B']
head1 = 0
head2 = 0
state = 0
accepting_state = 8 # State akhir untuk menghentikan mesin Turing

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
def binary_logarithm():
    global state
    if state == 0:
        if tape1[head1] == '0' and tape2[head2] == 'B':
            action('B', 'B', 'R', 'S',  1)
        elif tape1[head1] == '1' and tape2[head2] == 'B':
            action('1', 'B', 'R', 'S', accepting_state)
    elif state == 1:
        if tape1[head1] == '0' and tape2[head2] == 'B':
            action('0', 'B', 'R', 'S', 1)
        elif tape1[head1] == '1' and tape2[head2] == 'B':
            action('1', 'B', 'R', 'S', 2)
    elif state == 2:
        if tape1[head1] == '0' and tape2[head2] == 'B':
            action('0', 'B', 'R', 'S', 2)
        elif tape1[head1] == 'X' and tape2[head2] == 'B':
            action('X', 'B', 'R', 'S', 2)
        elif tape1[head1] == '1' and tape2[head2] == 'B':
            action('1', 'B', 'L', 'S', 3)
    elif state == 3:
        if tape1[head1] == 'X' and tape2[head2] == 'B':
            action('X', 'B', 'L', 'S', 3)
        elif tape1[head1] == '0' and tape2[head2] == 'B':
            action('X', 'B', 'L', 'S', 4)
    elif state == 4:
        if tape1[head1] == '0' and tape2[head2] == 'B':
            action('0', 'B', 'L', 'S', 5)
        elif tape1[head1] == '1' and tape2[head2] == 'B':
            action('1', 'B', 'R', 'S', 6)
    elif state == 5:
        if tape1[head1] == '0' and tape2[head2] == 'B':
            action('0', 'B', 'L', 'S', 5)
        elif tape1[head1] == '1' and tape2[head2] == 'B':
            action('1', 'B', 'L', 'S', 5)
        elif tape1[head1] == 'B' and tape2[head2] == 'B':
            action('B', 'B', 'R', 'S', 0)
    elif state == 6:
        if tape1[head1] == '0' and tape2[head2] == 'B':
            action('0', 'B', 'L', 'S', 6)
        elif tape1[head1] == 'X' and tape2[head2] == 'B':
            action('0', 'B', 'R', 'S', 6)
        elif tape1[head1] == '1' and tape2[head2] == 'B':
            action('1', '0', 'L', 'R', 7)
    elif state == 7:
        if tape1[head1] == '0' and tape2[head2] == 'B':
            action('0', 'B', 'L', 'S', 7)
        elif tape1[head1] == '1' and tape2[head2] == 'B':
            action('1', 'B', 'L', 'S', 7)
        elif tape1[head1] == 'B' and tape2[head2] == 'B':
            action('B', 'B', 'R', 'S', 0)


# Program utama untuk menjalankan mesin Turing sampai mencapai state accepting_state
while state != accepting_state:
    binary_logarithm()

# Output hasil akhir
print("Final tape1:",''.join(tape1))
print("Final tape2:",''.join(tape2))
print("Final state:", state)
print("Head1 position:", head1)
print("Head2 position:", head2)