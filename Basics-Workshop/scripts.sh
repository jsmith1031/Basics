
# Get the dates for the lastest issues from the wolfSSL github repository
./githubapi-get.sh $GITHUBTOKEN /repos/wolfSSL/wolfssl/issues | grep "created_at"

# Get quick summary of the latest updates to a very popular C++ programming repo
./githubapi-get.sh $GITHUBTOKEN /repos/federico-busato/Modern-CPP-Programming/commits | tail -n 400 | grep "message"