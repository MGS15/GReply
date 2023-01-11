# -*- coding: utf-8 -*-
"""
	@Author:	Soufiane Elkhamlichi
	@Date:		11/08/2022
	@Credit:	Soufiane Elkhamlichi
	@Links:		https://github.com/MGS15/
"""

from init.init_globals import COLORS, ACTIONS
from app import route
import sys

def print_help():
	print(f"""
		{COLORS.DODGER_BLUE_2 + COLORS.BOLD}--login{COLORS.DEFAULT} : {COLORS.BOLD}Create chrome profiles and login to accounts.{COLORS.DEFAULT}
		{COLORS.DODGER_BLUE_2 + COLORS.BOLD}--filter{COLORS.DEFAULT} : {COLORS.BOLD}Create / Update account's inbox filter.{COLORS.DEFAULT}
		{COLORS.DODGER_BLUE_2 + COLORS.BOLD}--config{COLORS.DEFAULT} : {COLORS.BOLD}Create / Update account's config, including:{COLORS.DEFAULT}
				{COLORS.DODGER_BLUE_2}+{COLORS.DEFAULT} From alias.
				{COLORS.DODGER_BLUE_2}+{COLORS.DEFAULT} Conversation view.
		{COLORS.DODGER_BLUE_2 + COLORS.BOLD}--send{COLORS.DEFAULT}   : {COLORS.BOLD}Start sending messages.{COLORS.DEFAULT}
		{COLORS.DODGER_BLUE_2 + COLORS.BOLD}--alias{COLORS.DEFAULT}   : {COLORS.BOLD}Randomize accounts aliases.{COLORS.DEFAULT}
		{COLORS.DODGER_BLUE_2 + COLORS.BOLD}--bounce{COLORS.DEFAULT}   : {COLORS.BOLD}Extract bounced emails from accounts.{COLORS.DEFAULT}
	""")

def args_error():
	print(f"{COLORS.RED}Invalid arguments!\nTry \"{COLORS.BOLD}--help{COLORS.DEFAULT + COLORS.RED}\" for more information!{COLORS.DEFAULT}")

def get_args() -> int:
	argc = len(sys.argv)
	if argc == 1:
		args_error()
		return ACTIONS.ERROR
	elif argc == 2:
		if sys.argv[1] == '--help':
			print_help()
			return ACTIONS.HELP
		elif sys.argv[1] == '--login':
			return ACTIONS.LOGIN
		elif sys.argv[1] == '--filter':
			return ACTIONS.FILTER
		elif sys.argv[1] == '--config':
			return ACTIONS.CONFIG
		elif sys.argv[1] == '--send':
			return ACTIONS.SEND
		elif sys.argv[1] == '--alias':
			return ACTIONS.ALIAS
		elif sys.argv[1] == '--bounce':
			return ACTIONS.BOUNCE
		else:
			args_error()
			return ACTIONS.ERROR
	elif argc == 3:
		if '--filter' in sys.argv and '--config' in sys.argv:
			return ACTIONS.FILTER + ACTIONS.CONFIG
		else:
			args_error()
			return ACTIONS.ERROR
	else:
		args_error()
		return ACTIONS.ERROR
	

def main():
	args_res = get_args()
	if args_res == ACTIONS.ERROR:
		exit(1)
	elif args_res == ACTIONS.HELP:
		return
	route.entry_point(args_res)

if __name__ == "__main__":
	main()
	exit(0)