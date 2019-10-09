### "Help, I keep getting a 'Permission Denied (publickey)' error when I push!"
This means, on your local machine, you haven't made any SSH keys. Not to worry. Here's how to fix:

1. Open git bash (Use the Windows search. To find it, type "git bash") or the Mac Terminal. Pro Tip: You can use any *nix based command prompt (but not the default Windows Command Prompt!)
2. Type cd ~/.ssh. This will take you to the root directory for Git (Likely C:\Users\[YOUR-USER-NAME]\.ssh\ on Windows)
3. Within the .ssh folder, there should be these two files: id_rsa and id_rsa.pub. These are the files that tell your computer how to communicate with GitHub, BitBucket, or any other Git based service. Type ls to see a directory listing. If those two files don't show up, proceed to the next step. NOTE: Your SSH keys must be named id_rsa and id_rsa.pub in order for Git, GitHub, and BitBucket to recognize them by default.
4. To create the SSH keys, type ssh-keygen -t rsa -C "your_email@example.com". This will create both id_rsa and id_rsa.pub files.
5. Now, go and open id_rsa.pub in your favorite text editor (you can do this via Windows Explorer or the OSX Finder if you like, typing open . will open the folder).
6. Copy the contents--exactly as it appears, with no extra spaces or lines--of id_rsa.pub and paste it into GitHub and/or BitBucket under the Account Settings > SSH Keys. NOTE: I like to give the SSH key a descriptive name, usually with the name of the workstation I'm on along with the date.
7. Now that you've added your public key to Github and/or BitBucket, try to git push again and see if it works. It should!
8. More help available from [GitHub on creating SSH Keys](https://help.github.com/en/articles/connecting-to-github-with-ssh) and [BitBucket Help](https://confluence.atlassian.com/bitbucket/set-up-ssh-for-git-728138079.html)
