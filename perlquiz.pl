use strict;
use warnings;
use LWP::UserAgent;
use HTML::TreeBuilder;

# Ask user for URL input
print "Enter the URL to scrape: ";
chomp(my $url = <STDIN>);

# Create a UserAgent
my $ua = LWP::UserAgent->new;
$ua->agent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36");

# Fetch the webpage
my $response = $ua->get($url);

# Check if request was successful
if (!$response->is_success) {
    die "Could not fetch page: " . $response->status_line . "\n";
}

# Get HTML content
my $html = $response->decoded_content;

# Parse HTML
my $tree = HTML::TreeBuilder->new;
$tree->parse($html);

# Extract and display headlines
print "\nHeadlines from $url:\n";
foreach my $headline ($tree->look_down(_tag => 'h1')) {
    print "- ", $headline->as_text, "\n";
}
foreach my $link ($tree->look_down(_tag => 'a')) {
    print "- ", $link->as_text, "\n";
}

# Clean up
$tree->delete;
