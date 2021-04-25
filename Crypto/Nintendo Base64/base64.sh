#!/bin/bash

encoded_text="Vm0xNFlWVXhSWGxUV0doWVlrZFNWRmx0ZUdGalZsSlZWR3RPYWxKdGVIcFdiR2h2VkdzeFdGVnViRmRXTTFKeVdWUkdZV1JGT1ZWVmJGWk9WakpvV1ZaclpEUlVNVWw0Vkc1U1RsWnNXbGhWYkZKWFUxWmFSMWRzV2s1V2F6VkpWbTEwYjFkSFNsbFZiRkpXWWtaYU0xcEZXbUZTTVZaeVkwVTFWMDFHYjNkV2EyTXhWakpHVjFScmFGWmlhM0JYV1ZSR1lWZEdVbFZTYms1clVsUldTbGRyV2tkV2JGcEZVVlJWUFE9PQ=="
flag=$encoded_text

#Iterate until we find the flag
while true
do
	#To check whether the decoded text contains the flag format in it
	if grep "CHTB" <<< "$flag" 
	then
		echo "$flag"
		break
	fi
	#Updating the value of flag variable
	flag=$(echo "$flag" | base64 --decode) 
done