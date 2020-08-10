# -*- coding: UTF-8 -*-
import re
def get_place_num(id_card):
	if id_card[0] == 'A':
		return 10
	elif id_card[0] == 'B':
		return 11
	elif id_card[0] == 'C':
		return 12
	elif id_card[0] == 'D':
		return 13
	elif id_card[0] == 'E':
		return 14
	elif id_card[0] == 'F':
		return 15
	elif id_card[0] == 'G':
		return 16
	elif id_card[0] == 'H':
		return 17
	elif id_card[0] == 'I':
		return 34
	elif id_card[0] == 'J':
		return 18
	elif id_card[0] == 'K':
		return 19
	elif id_card[0] == 'L':
		return 20
	elif id_card[0] == 'M':
		return 21
	elif id_card[0] == 'N':
		return 22
	elif id_card[0] == 'O':
		return 35
	elif id_card[0] == 'P':
		return 23
	elif id_card[0] == 'Q':
		return 24
	elif id_card[0] == 'R':
		return 25
	elif id_card[0] == 'S':
		return 26
	elif id_card[0] == 'T':
		return 27
	elif id_card[0] == 'U':
		return 28
	elif id_card[0] == 'V':
		return 29
	elif id_card[0] == 'W':
		return 32
	elif id_card[0] == 'X':
		return 30
	elif id_card[0] == 'Y':
		return 31
	elif id_card[0] == 'Z':
		return 33

def check_id_card(id_card):
	id_card = str(id_card)
	id_card.upper()
	id_card = id_card.strip()  # 刪除前後空格
	id_card_list = list(id_card)

	# 地區校驗
	if not get_place_num(id_card[0:1]):
		print(errors[1])
	# 15位身份號碼檢測
	if len(id_card) == 10:
		if (int(str(get_place_num(id_card[0]))[0]) + int(str(get_place_num(id_card[0]))[1])*9 + int(id_card[1])*8 + int(id_card[2])*7 + int(id_card[3])*6 + int(id_card[4])*5 + int(id_card[5])*4 + int(id_card[6])*3 + int(id_card[7])*2+ int(id_card[8])+ int(id_card[9])) %10 ==0:
			print('正確的身份證字號')
		else:
			print(errors[0])
	elif len(id_card) > 10:
			print(errors[2])
	elif len(id_card) < 10:
			print(errors[3])
errors = ['身份證字號錯誤' , '沒有這地區' , '多打了數字' , '少打了數字']
while True:
	input_card = raw_input('請輸入你的身份證字號:')
	if input_card == "exit":
		print('程式已結束！')
		break
	else:
		check_id_card(input_card)
