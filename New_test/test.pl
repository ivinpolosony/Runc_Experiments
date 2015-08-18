#!/usr/bin/perl
use IO::Handle;
my $filename = 'report.txt';

open(my $fh, '>', $filename) or die "Could not open file '$filename' $!";
for (my $i=1; $i <= 300; $i++) {
        print $fh "i is $i\n";
        $fh->flush();
        sleep 1;
	print $i;
}
close $fh;
