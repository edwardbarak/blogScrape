# blogScrape

## Instructions
1. Run the script
2. Enter the URL of the post you want to start from
3. Enter the text of the link that goes to the next page

## Additional notes and explanations
- Posts will be generated in the script's directory with the naming format "Post_N.txt"
- The script uses bs4 to grab the text within \<p\> tags, then writes that out to a file
- The script looks for an \<a\> tag that has the inputted "text of the link" to find the next page
- The script terminates when it can no longer find an <a> tag that matches the "text of link" criteria
gt'
## IDC License
I don't care.



# Blog Scrape
> Python library to extract contents from blogs

Writes blog post text to file, then goes to the next blog post and does it again until there aren't anymore posts.When

## Installation
Insert BlogScrape.py into the directory you want to use it in, then ```import BlogScrape.py``` like usual.

## Usage example

```BlogScrape.text.recursiveA('example.blog.com/post10/', 'Next Post')```
Function will go to the URL 'example.blog.com/post10/' and extract all text from that page. Then it will find the first **\<a\>** that contains the string 'Next Post', and access the associated href to recursively repeat the process. Function self terminates when no more posts are available.

```BlogScrape.text.allA('example.blog.com/post10/', ```

