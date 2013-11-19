#!/usr/bin/perl

unshift @INC,  'C:\Users\Dylan\Dropbox\Game Dev Stuff\The Folder Of Bob Dole\Python and Perl\Tic Tac Toe\perl';
use lib 'C:\Users\Dylan\Dropbox\Game Dev Stuff\The Folder Of Bob Dole\Python and Perl\Tic Tac Toe\perl';
use strict;
use warnings;
use TTTGame::TTTPosChecker::EndGame3x3; 
use TTTGame::TTTPosChecker::EndGame4x4; 

my @board3x3_1 = [
							'1', '2', '3',
							'4', '5', '6',
							'7', '8', '9' 
							];
							
my @board4x4_1 = [
							 '1',  '2',  '3',  '4',
							 '5',  '6',	 '7',  '8', 
							 '9', '10', '11', '12',
							'13', '14', '15', '16'
							];				
					
print TTTGame::TTTPosChecker::EndGame3x3::is_game_over(\@board3x3_1), "\n";

print TTTGame::TTTPosChecker::EndGame3x3::is_win_for_x(\@board3x3_1), "\n";

print TTTGame::TTTPosChecker::EndGame3x3::is_win_for_o(\@board3x3_1), "\n"; 

print TTTGame::TTTPosChecker::EndGame4x4::is_game_over(\@board4x4_1), "\n";

print TTTGame::TTTPosChecker::EndGame4x4::is_win_for_x(\@board4x4_1), "\n";

print TTTGame::TTTPosChecker::EndGame4x4::is_win_for_o(\@board4x4_1), "\n";
