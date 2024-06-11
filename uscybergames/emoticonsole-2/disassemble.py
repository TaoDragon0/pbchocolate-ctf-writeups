import sys

class EmoDisassembly:

    def __init__(self, F):
        self.P = []
        i = 0
        while i < len(F):
            I = F[i]
            if I in ['📈', '📉', '📰', '📞', '🔊', '📥']:
                self.P.append(F[i:i + 2])
                i += 2
            elif I in ['📕', '📝', '🟰', '🔃']:
                self.P.append(F[i:i + 3])
                i += 3
            elif I in ['🔄', '🔁', '🔼']:
                self.P.append(F[i:i + 4])
                i += 4
            elif I in ['➖', '➕', '➗', '⊕', '🚀', '🎎', '🏮']:
                self.P.append(F[i:i + 4])
                i += 4
            elif I in ['≫', '≪']:
                self.P.append(F[i:i + 5])
                i += 5
            else:
                self.P.append(I)
                i += 1
        self.NUMS = {'⓿': '0', '⓵': '1', '⓶': '2', '⓷': '3', '⓸': '4', '⓹': '5', '⓺': '6', '⓻': '7', '⓼': '8', '⓽': '9'}
        self.EMO = {'🌞': self.emo_func_start, '📥': self.emo_func_input_byte, '🔼': self.emo_func_push_byte, '⊕': self.emo_func_xor_byte, '❔': self.emo_func_if, '🚫': self.emo_func_if_not, '🟰': self.emo_func_compare, '≪': self.emo_func_shift_left, '≫': self.emo_func_shift_right, '🎎': self.emo_func_and, '🏮': self.emo_func_or, '🔃': self.emo_func_swap_mem, '🔄': self.emo_func_jump_back, '🔁': self.emo_func_jump_forward, '📈': self.emo_func_mov_to_register, '📰': self.emo_func_copy_to_register, '📉': self.emo_func_mov_from_register, '📎': self.emo_func_push_pc, '📌': self.emo_func_pop_to_pc, '🚀': self.emo_func_absolute_jump, '📝': self.emo_func_write_memory, '📕': self.emo_func_read_memory, '➖': self.emo_func_subtract, '➕': self.emo_func_add, '➗': self.emo_func_mod, '🔊': self.emo_func_output_byte, '📞': self.emo_func_call, '🪄': self.emo_func_return, '🌛': self.emo_func_exit, '🗑': self.emo_func_nop}

    def emo_func_start(self, I):
        return '#start'

    def emo_func_input_byte(self, I):
        return f'input r{int(self.NUMS[I[1]]) - 1}'

    def emo_func_push_byte(self, I):
        return 'push ' + ''.join([self.NUMS[I[i]] for i in range(1, 4)])

    def emo_func_push_pc(self, I):
        return 'push pc'

    def emo_func_swap_mem(self, I):
        R1 = int(self.NUMS[I[1]]) - 1
        R2 = int(self.NUMS[I[2]]) - 1
        return f'swap [{R1}] [{R2}]'

    def emo_func_absolute_jump(self, I):
        R1 = int(self.NUMS[I[1]]) - 1
        return f'jump r{R1}'

    def emo_func_pop_to_pc(self, I):
        return 'pop pc'

    def emo_func_call(self, I):
        R1 = int(self.NUMS[I[1]]) - 1
        return f'call r{R1}'

    def emo_func_nop(self, I):
        return 'nop'

    def emo_func_return(self, I):
        return 'return'

    def emo_func_xor_byte(self, I):
        R1 = int(self.NUMS[I[1]]) - 1
        R2 = int(self.NUMS[I[2]]) - 1
        R3 = int(self.NUMS[I[3]]) - 1
        return f'r{R3} = r{R1} ^ r{R2}'
        self.R[R3] = self.R[R1] ^ self.R[R2]

    def emo_func_and(self, I):
        R1 = int(self.NUMS[I[1]]) - 1
        R2 = int(self.NUMS[I[2]]) - 1
        R3 = int(self.NUMS[I[3]]) - 1
        return f'r{R3} = r{R1} & r{R2}'
        self.R[R3] = self.R[R1] & self.R[R2]

    def emo_func_or(self, I):
        R1 = int(self.NUMS[I[1]]) - 1
        R2 = int(self.NUMS[I[2]]) - 1
        R3 = int(self.NUMS[I[3]]) - 1
        return f'r{R3} = r{R1} | r{R2}'
        self.R[R3] = self.R[R1] | self.R[R2]

    def emo_func_shift_left(self, I):
        R = int(self.NUMS[I[1]]) - 1
        V = int(''.join([self.NUMS[I[i]] for i in range(2, 5)]))
        return f'r{R} <<= {V}'
        self.R[R] <<= V

    def emo_func_shift_right(self, I):
        R = int(self.NUMS[I[1]]) - 1
        V = int(''.join([self.NUMS[I[i]] for i in range(2, 5)]))
        return f'r{R} >>= {V}'
        self.R[R] >>= V

    def emo_func_compare(self, I):
        R1 = int(self.NUMS[I[1]]) - 1
        R2 = int(self.NUMS[I[2]]) - 1
        return f'cmp r{R1} r{R2}'
        if self.R[R1] == self.R[R2]:
            self.ACC = 1
        else:
            self.ACC = 0

    def emo_func_if(self, I):
        return f'if'
        if self.ACC == 0:
            self.PC += 1

    def emo_func_if_not(self, I):
        return f'ifnot'
        if self.ACC == 1:
            self.PC += 1

    def emo_func_jump_back(self, I):
        X = int(''.join([self.NUMS[I[i]] for i in range(1, 4)]))
        return f'jumpback {X}'
        self.PC -= X

    def emo_func_jump_forward(self, I):
        X = int(''.join([self.NUMS[I[i]] for i in range(1, 4)]))
        return f'jumpforward {X}'
        self.PC += X

    def emo_func_mov_to_register(self, I):
        R1 = int(self.NUMS[I[1]]) - 1
        return f'pop r{R1}'
        self.R[R1] = self.STACK.pop()

    def emo_func_copy_to_register(self, I):
        R1 = int(self.NUMS[I[1]]) - 1
        return f'copy r{R1}'
        self.R[R1] = self.STACK[-1]

    def emo_func_mov_from_register(self, I):
        R1 = int(self.NUMS[I[1]]) - 1
        return f'push r{R1}'
        self.STACK.append(self.R[R1])

    def emo_func_subtract(self, I):
        R1 = int(self.NUMS[I[1]]) - 1
        R2 = int(self.NUMS[I[2]]) - 1
        R3 = int(self.NUMS[I[3]]) - 1
        return f'r{R3} = r{R1} - r{R2}'
        self.R[R3] = self.R[R1] - self.R[R2]

    def emo_func_add(self, I):
        R1 = int(self.NUMS[I[1]]) - 1
        R2 = int(self.NUMS[I[2]]) - 1
        R3 = int(self.NUMS[I[3]]) - 1
        return f'r{R3} = r{R1} + r{R2}'
        self.R[R3] = self.R[R1] + self.R[R2]

    def emo_func_mod(self, I):
        R1 = int(self.NUMS[I[1]]) - 1
        R2 = int(self.NUMS[I[2]]) - 1
        R3 = int(self.NUMS[I[3]]) - 1
        return f'r{R3} = r{R1} + r{R2}'
        self.R[R3] = self.R[R1] % self.R[R2]

    def emo_func_write_memory(self, I):
        R1 = int(self.NUMS[I[1]]) - 1
        R2 = int(self.NUMS[I[2]]) - 1
        return f'[r{R2}] = r{R1}'
        self.MEM[self.R[R2]] = self.R[R1]

    def emo_func_read_memory(self, I):
        R1 = int(self.NUMS[I[1]]) - 1
        R2 = int(self.NUMS[I[2]]) - 1
        return f'r{R2} = [r{R1}]'
        self.R[R2] = self.MEM[self.R[R1]]

    def emo_func_output_byte(self, I):
        R1 = int(self.NUMS[I[1]]) - 1
        return f'print {R1}'
        sys.stdout.write(chr(self.R[R1]))

    def emo_func_exit(self, I):
        return 'exit'

    def disassemble_program(self):
        self.PC = 0
        self.dis = []
        while True:
            if len(self.P) == len(self.dis):
                break
            I = self.P[self.PC]
            fn = self.EMO.get(I[0], None)
            if fn is not None:
                a = fn(I)
                self.dis.append(f'{self.PC} {a}')
                print(self.dis[-1])
                self.PC += 1
            else:
                self.dis.append(f'invalid {I[0]}')
        return self.dis
if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Usage: ./disassemble.py input_file.emo')
        sys.exit(1)
    try:
        F = open(sys.argv[1], 'r').read()
        program = EmoDisassembly(F)
        dis = program.disassemble_program()
    except FileNotFoundError:
        print('Unable to open input file.')
