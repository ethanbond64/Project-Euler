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

        # 0 index is real, 1 index is for guess and check
        self.mat = [np.zeros((9,9),dtype='int'),np.zeros((9,9),dtype='int')]
        self.cache = [np.zeros((9,9,9)),np.zeros((9,9,9))]
        self.solved = [0,0]

        self.rounds = 0

        for idx in range(len(raw)):
            i = idx // 9
            j = idx % 9
            n = raw[idx]
            if n != '0':
                self.place_num(i,j,int(n),0)

    def get_cube(self,row,col):
        return self.mat[0][row*3:(row*3)+3,col*3:(col*3)+3]

    def get_answer(self):
        row = self.get_cube(0,0)[0]
        val_str = ''.join([str(i) for i in row])
        if '0' not in val_str:
            return int(val_str)
        return None

    # small rows, cols: 0-8
    def place_num(self,row,col,n,temp_idx):
        # place in main mat
        self.mat[temp_idx][row,col] = n

        # Convert to index mode, zero index
        n -= 1

        # Confirm this number
        self.cache[temp_idx][row,col,n] = CONFIRMED
        
        # All in the same small box are invalid 
        self.cache[temp_idx][row,col,:n] = INVALID
        self.cache[temp_idx][row,col,n+1:] = INVALID
        
        # All same in the same row are invalid
        self.cache[temp_idx][row,:col,n] = INVALID
        self.cache[temp_idx][row,col+1:,n] = INVALID

        # All same in the same col are invalid
        self.cache[temp_idx][:row,col,n] = INVALID
        self.cache[temp_idx][row+1:,col,n] = INVALID
        
        # All in the same big box are invalid
        box_r = row // 3
        box_c = col // 3 

        for r in range(box_r*3,(box_r*3)+3):
            for c in range(box_c*3,(box_c*3)+3):
                if r != row and c != col:
                    self.cache[temp_idx][r,c,n] = INVALID

        self.solved[temp_idx] += 1


    def do_round(self,temp_idx):
        # find where sums to -8
        for i in range(9):
            for j in range(9):
                if np.sum(self.cache[temp_idx][i,j,:]) == -8:
                    n = np.where(self.cache[temp_idx][i,j]==0)[0][0]+1
                    self.place_num(i,j,n,temp_idx)
                    # print('ROW:',i+1,'COL:',j+1,'VAL:',np.where(self.cache[i,j]==0)[0][0]+1)
               
                if np.sum(self.cache[temp_idx][i,:,j]) == -8:
                    c = np.where(self.cache[temp_idx][i,:,j]==0)[0][0]
                    self.place_num(i,c,j+1,temp_idx)
                    # print('ROW:',i+1,'COL:',np.where(self.cache[i,:,j]==0)[0][0]+1,'VAL:',j+1)
                
                if np.sum(self.cache[temp_idx][:,i,j]) == -8:
                    r = np.where(self.cache[temp_idx][:,i,j]==0)[0][0]
                    self.place_num(r,i,j+1,temp_idx)
                    # print('ROW:',np.where(self.cache[:,i,j]==0)[0][0]+1,'COL:',i+1,'VAL:',j+1)

        self.rounds += 1
        # print(self.rounds,' Solved:',self.solved)

    def attempt_round(self,first):
        # print('START ATTEMPT ON PUZZLE NO:',self.puzzlenum)
        # print('CURRENTLY SOLVED: ',self.solved)

        # Create copy matrix/cache to work on
        if first:
            self.mat[1] = copy.deepcopy(self.mat[0])
            self.cache[1] = copy.deepcopy(self.cache[0])
            self.solved[1] = copy.deepcopy(self.solved[0])

        # Try the first 0
        loc = np.where(self.cache[1] == 0)
        self.place_num(loc[0][0],loc[1][0],loc[2][0]+1,1)

        # fill in 6 rounds
        self.do_round(1)
        self.do_round(1)
        self.do_round(1)
        self.do_round(1)
        self.do_round(1)
        self.do_round(1)
        

        # check for -9
        # if exists learn from attempt
        # else save old mat as new
        bad = False
        for i in range(9):
            for j in range(9):
                if np.sum(self.cache[1][i,j,:]) == -9:
                    bad = True
                    break
                if np.sum(self.cache[1][i,:,j]) == -9:
                    bad = True
                    break
                if np.sum(self.cache[1][:,i,j]) == -9:
                    bad = True
                    break
            if bad:
                break
        
        loc2 = np.where(self.cache[1] == 0)

        if len(loc2[0]) == 0 and self.solved[1] != 81:
            bad = True

        if not bad:
            # print('Updating after test')
            if self.solved[1] == 81:
                self.cache[0] = copy.deepcopy(self.cache[1])
                self.mat[0] = copy.deepcopy(self.mat[1])
                self.solved[0] = copy.deepcopy(self.solved[1])
                return True
            else:
                return self.attempt_round(False)
        else:
            # Learn from it
            # print('TEST IS BAD')
            self.cache[0][loc[0][0],loc[1][0],loc[2][0]] = INVALID
            return False


def parse_input(txt):
    ugly = re.split('Grid\s\d+',txt) 
    str_arrs = [u.replace('\n','') for u in ugly][1:]

    return str_arrs

file = open(os.path.split(os.path.abspath(__file__))[0] + '/p096_sudoku.txt','r')

raw_puzzles = parse_input(file.read())

final_score = 0
total_solved = 0
for idx,puzzle in enumerate(raw_puzzles):

    p = Puzzle(idx,puzzle)

    last_solved = 0
    while(p.solved[0] != 81):
        p.do_round(0)
        if last_solved == p.solved[0]:

            # print(':( reached local max')
            p.attempt_round(True)

        last_solved = p.solved[0]

    if p.get_answer() is not None:
        total_solved += 1
        final_score += p.get_answer()

print('Final Score')
print(final_score)
print('Total Solved')
print(total_solved,'/ 50')