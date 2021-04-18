import os
import re
import numpy as np
import copy

UNTOUCHED = 0
INVALID = -1
CONFIRMED = 1


class Puzzle:

    def __init__(self,n,raw):
        self.puzzlenum = n
        self.raw = raw
        self.arr = [raw[i*9:(i+1)*9] for i in range(9)]
        # self.mat = np.array([list(row) for row in self.arr],dtype='int')
        self.mat = np.zeros((9,9),dtype='int')
        self.cache = np.zeros((9,9,9))
        self.rounds = 0
        self.solved = 0
        self.temp_solved = 0
        self.mat_copy = np.zeros((9,9),dtype='int')
        self.cache_copy = np.zeros((9,9,9))

        for idx in range(len(raw)):
            i = idx // 9
            j = idx % 9
            n = raw[idx]
            if n != '0':
                self.place_num(i,j,int(n))

    def get_cube(self,row,col):
        return self.mat[row*3:(row*3)+3,col*3:(col*3)+3]

    # big rows 0-2
    def get_row(self,row):
        return self.mat[row*3:(row*3)+3,:]

    # big cols 0-2
    def get_col(self,col):
        return self.mat[:,col*3:(col*3)+3]

    def get_answer(self):
        row = self.get_cube(0,0)[0]
        val_str = ''.join([str(i) for i in row])
        if '0' not in val_str:
            return int(val_str)
        return None

    # small rows, cols: 0-8
    def place_num(self,row,col,n):
        # place in main mat
        self.mat[row,col] = n

        # print(n,row,col)
        # Convert to index mode, zero index
        n -= 1

        # Confirm this number
        self.cache[row,col,n] = CONFIRMED
        
        # All in the same small box are invalid 
        self.cache[row,col,:n] = INVALID
        self.cache[row,col,n+1:] = INVALID
        
        # All same in the same row are invalid
        self.cache[row,:col,n] = INVALID
        self.cache[row,col+1:,n] = INVALID

        # All same in the same col are invalid
        self.cache[:row,col,n] = INVALID
        self.cache[row+1:,col,n] = INVALID
        
        # All in the same big box are invalid
        box_r = row // 3
        box_c = col // 3 
        # print('NEW')
        # print(box_r,box_c)
        # print('avoid',row,col)
        # print('----')
        f = 0
        for r in range(box_r*3,(box_r*3)+3):
            for c in range(box_c*3,(box_c*3)+3):
                if r != row and c != col:
                    # print(r,c)
                    f+= 1
                    self.cache[r,c,n] = INVALID
        if f != 4:
            print('WE GOTTA PRBLM')
        self.solved += 1

    # small rows, cols: 0-8
    def place_check_num(self,row,col,n):
        # place in main mat
        self.mat_copy[row,col] = n

        # print(n,row,col)
        # Convert to index mode, zero index
        n -= 1

        # Confirm this number
        self.cache_copy[row,col,n] = CONFIRMED
        
        # All in the same small box are invalid 
        self.cache_copy[row,col,:n] = INVALID
        self.cache_copy[row,col,n+1:] = INVALID
        
        # All same in the same row are invalid
        self.cache_copy[row,:col,n] = INVALID
        self.cache_copy[row,col+1:,n] = INVALID

        # All same in the same col are invalid
        self.cache_copy[:row,col,n] = INVALID
        self.cache_copy[row+1:,col,n] = INVALID
        
        # All in the same big box are invalid
        box_r = row // 3
        box_c = col // 3 
        # print('NEW')
        # print(box_r,box_c)
        # print('avoid',row,col)
        # print('----')
        f = 0
        for r in range(box_r*3,(box_r*3)+3):
            for c in range(box_c*3,(box_c*3)+3):
                if r != row and c != col:
                    # print(r,c)
                    f+= 1
                    self.cache_copy[r,c,n] = INVALID
        # if f != 4:
        #     print('WE GOTTA PRBLM')
        self.temp_solved += 1

    def do_round(self):
        # find where sums to -8
        for i in range(9):
            for j in range(9):
                if np.sum(self.cache[i,j,:]) == -8:
                    n = np.where(self.cache[i,j]==0)[0][0]+1
                    self.place_num(i,j,n)
                    # print('ROW:',i+1,'COL:',j+1,'VAL:',np.where(self.cache[i,j]==0)[0][0]+1)
                if np.sum(self.cache[i,:,j]) == -8:
                    c = np.where(self.cache[i,:,j]==0)[0][0]
                    self.place_num(i,c,j+1)
                    # print('ROW:',i+1,'COL:',np.where(self.cache[i,:,j]==0)[0][0]+1,'VAL:',j+1)
                if np.sum(self.cache[:,i,j]) == -8:
                    r = np.where(self.cache[:,i,j]==0)[0][0]
                    self.place_num(r,i,j+1)
                    # print('ROW:',np.where(self.cache[:,i,j]==0)[0][0]+1,'COL:',i+1,'VAL:',j+1)

        self.rounds += 1
        print(self.rounds,' Solved:',self.solved)

    def do_check_round(self):
        # find where sums to -8
        for i in range(9):
            for j in range(9):
                if np.sum(self.cache_copy[i,j,:]) == -8:
                    n = np.where(self.cache_copy[i,j]==0)[0][0]+1
                    self.place_check_num(i,j,n)
                    # print('ROW:',i+1,'COL:',j+1,'VAL:',np.where(self.cache[i,j]==0)[0][0]+1)
                if np.sum(self.cache_copy[i,:,j]) == -8:
                    c = np.where(self.cache_copy[i,:,j]==0)[0][0]
                    self.place_check_num(i,c,j+1)
                    # print('ROW:',i+1,'COL:',np.where(self.cache[i,:,j]==0)[0][0]+1,'VAL:',j+1)
                if np.sum(self.cache_copy[:,i,j]) == -8:
                    r = np.where(self.cache_copy[:,i,j]==0)[0][0]
                    self.place_check_num(r,i,j+1)
                    # print('ROW:',np.where(self.cache[:,i,j]==0)[0][0]+1,'COL:',i+1,'VAL:',j+1)

        # self.rounds += 1
        print(self.rounds,' Solved:',self.solved)

    def attempt_round(self,first):
        print('START ATTEMPT ON PUZZLE NO:',self.puzzlenum)
        print('CURRENTLY SOLVED: ',self.solved)
        # Create copy matrix/cache to work on
        if first:
            self.mat_copy = copy.deepcopy(self.mat)
            self.cache_copy = copy.deepcopy(self.cache)
            self.temp_solved = copy.deepcopy(self.solved)

        # Go for one of the first 3 numbers
        # Try the first 0
        loc = np.where(self.cache_copy == 0)
        print(len(loc))
        print(len(loc[0]))
        print(self.mat)
        print(self.cache)
        # if len(loc[0]) == 0:
        #     print('LOOK')
        #     print(self.temp_solved)
            # return
        print(loc[0][0],loc[1][0],loc[2][0])
        # print(self.cache_copy[:3,:3,:])
        self.place_check_num(loc[0][0],loc[1][0],loc[2][0]+1)

        # fill in 6 rounds
        self.do_check_round()
        self.do_check_round()
        self.do_check_round()
        self.do_check_round()
        self.do_check_round()
        

        # check for -9
        # if exists learn from attempt
        # else save old mat as new
        bad = False
        for i in range(9):
            for j in range(9):
                if np.sum(self.cache_copy[i,j,:]) == -9:
                    bad = True
                    break
                    # print('ROW:',i+1,'COL:',j+1,'VAL:',np.where(self.cache[i,j]==0)[0][0]+1)
                if np.sum(self.cache_copy[i,:,j]) == -9:
                    bad = True
                    break
                    # print('ROW:',i+1,'COL:',np.where(self.cache[i,:,j]==0)[0][0]+1,'VAL:',j+1)
                if np.sum(self.cache_copy[:,i,j]) == -9:
                    bad = True
                    break
                    # print('ROW:',np.where(self.cache[:,i,j]==0)[0][0]+1,'COL:',i+1,'VAL:',j+1)
            if bad:
                break
        
        loc2 = np.where(self.cache_copy == 0)
        print('POST TEST 0 COUNT:',len(loc2[0]))

        if len(loc2[0]) == 0 and self.temp_solved != 81:
            bad = True

        if not bad:
            print('Updating after test')
            print('New solved: ',self.temp_solved)
            if self.temp_solved == 81:
                self.cache = copy.deepcopy(self.cache_copy)
                self.mat = copy.deepcopy(self.mat_copy)
                self.solved = copy.deepcopy(self.temp_solved)
                return True
            else:
                return self.attempt_round(False)
        else:
            # Learn from it
            print('TEST IS BAD')
            if len(loc2[0]) == 0:
                print('NO ZEROS LEFT')
            else:
                print('-9 ROW EXISTS')
            self.cache[loc[0][0],loc[1][0],loc[2][0]] = INVALID
            return False


def parse_input(txt):
    ugly = re.split('Grid\s\d+',txt) 
    # print(ugly)
    str_arrs = [u.replace('\n','') for u in ugly][1:]

    return str_arrs

file = open(os.path.split(os.path.abspath(__file__))[0] + '/p096_sudoku.txt','r')

raw_puzzles = parse_input(file.read())

final_score = 0
total_solved = 0
for idx,puzzle in enumerate(raw_puzzles):

    p = Puzzle(idx,puzzle)
    # p.do_round()
    # print(p.cache)
    last_solved = 0
    while(p.solved != 81):
        p.do_round()
        if last_solved == p.solved:
            print(':( reached local max')
            # print(p.mat)
            # print(p.mat_copy)
            p.attempt_round(True)
            print('change after attmept:',p.solved-last_solved)
            if p.solved == 81:
                print(p.mat)
            # break
        last_solved = p.solved


    print("Rounds:",p.rounds)
    # print(p.get_answer())
    if p.get_answer() is not None:
        total_solved += 1
        final_score += p.get_answer()
    else:
        pass
        # print(p.cache)
print('Final Score')
print(final_score)
print('Total Solved')
print(total_solved)
# print(p.cache)
# print(p.mat)
# print(p.get_cube(0,0))
# print(p.get_cube(1,1))
# print(p.get_cube(1,2))
# print(p.get_cube(2,2))
# print(p.get_row(0))
# print(p.get_col(0))
# print(p.get_row(1))
# print(p.get_col(1))
# print(p.get_row(2))
# print(p.get_col(2))
# print(p.get_answer())

# continuosly iterate through 9 boxes until solved

# check box, row, col 


