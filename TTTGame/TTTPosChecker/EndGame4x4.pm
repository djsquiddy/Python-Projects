#!/usr/bin/perl

package TTTGame::TTTPosChecker::EndGame4x4;

use lib "C:\Users\Dylan\Dropbox\Tic Tac Toe\perl\\";
use strict;
use warnings;

my @winning_compinations = [
				[ 0,  1,  2,  3],
				[ 4,  5,  6,  7],
				[ 8,  9, 10, 11],
				[12, 13, 14, 15],
				[ 0,  4,  8, 12],
				[ 1,  5,  9, 13],
				[ 2,  6, 10, 14],
				[ 3,  7, 11, 15],
				[10, 11, 12, 13],
				[ 0,  5, 10, 15],
				[ 3,  6,  9, 12] ];

sub is_game_over
{
	my $board = shift;
	
	if( ( is_win_for_o( $board ) ) or ( is_win_for_x( $board ) ) )
	{
		return 1;
	}
	else
	{
		foreach my $i ( @{$board} )
		{
			if(($i ne 'O') or ($i ne 'X'))
			{
				return 0;
			}
		}
		return 1;
	}
}

sub is_win_for_x
{
	my $board = shift;
	my $x_value = 'X';
	
	foreach my $w ( @winning_compinations )
	{
		my $isTrue = 0;
		foreach my $i ( @{$w} )
		{
			if(($board->[0][ @{$i}[0] ] eq $x_value) and ($board->[0][ @{$i}[1] ] eq $x_value) and ($board->[0][ @{$i}[2] ] eq $x_value))
			{
				$isTrue = 1;
				last;
			}
		}		
		
		if( $isTrue )
		{	
			my @list;
			foreach my $v ( $w )
			{
				push( @list, ( $v + 1 ));
			}			
			return 1;#, \@list; # [($v + 1) foreach my $v ( $w )];
		}
	}
	return 0;#[];
}

sub is_win_for_o
{
	my $board = shift;
	my $o_value = 'O';
	
	foreach my $w ( @winning_compinations )
	{
		my $isTrue = 0;
		foreach my $i ( @{$w} )
		{
			if(($board->[0][ @{$i}[0] ] eq $o_value) and ($board->[0][ @{$i}[1] ] eq $o_value) and ($board->[0][ @{$i}[2] ] eq $o_value))
			{
				$isTrue = 1;
				last;
			}
		}		
		
		if( $isTrue )
		{	
			my @list;
			foreach my $v ( $w )
			{
				push( @list, ( $v + 1 ));
			}			
			return 1;#, \@list; # [($v + 1) foreach my $v ( $w )];
		}
	}
	return 0;#[];
}
1;