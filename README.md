# Solutions-NFT-Puzzle-December-2021
This repository contains all scripts to solve the November 2021 NFT puzzle for whiteboardcrypto.com.

# Puzzle 01

The "File Modification Date/Time" of some images are different than others. When you check the modification date/time, the date for some images its 01:00:00 and 01:01:00. The minute represents a 0 or 1. Once you get all the 0's and 1's, you will get the flag in binary form.

:checkered_flag: WBC{A1NT_G0T_N0_T1ME_F0R_TH1S}<br>
:link: [Link](https://github.com/WhiteboardCryptoTeam/Solutions-NFT-Puzzle-December-2021/blob/main/WBC%20-%20Solution%20NFT%20Puzzle01%20December%202021.py) to the script. 

# Puzzle 02

Image 1824.png had some appended bytes at the end of the image. Every file can be identified by the "magic byte/file signature". This is the first few bytes of a file. If you look at the appended bytes, you can see it starts with WBC which isn't used as a file signature, but if you look closely, you can see many indications it should be a PNG file. So simply changing the WBC in bytes to PNG fixes the image. Once you open the image you will see a malformed QR code. The squares are not squares anymore, but it is changed to a circle. Changing the circle to a square fixes the QR code and it can be scanned. Once scanned, it displays the flag.

:checkered_flag: WBC{QR_C0D3_1S_FUN}<br>
:link: No script yet.

# Puzzle 03

Image 0.png and 4095.png contains the same total appended bytes. When you compare both appended bytes you can see a similarity. When you know to look for WBC{SOME_TEXT} it should be easy to see the last } in both files. This is a good indication that at some offsets the bytes are the same. If you take all bytes that are the same from both files, you will get the flag.

:checkered_flag: WBC{3V1L_TW1NS!}<br>
:link: [Link](https://github.com/WhiteboardCryptoTeam/Solutions-NFT-Puzzle-December-2021/blob/main/WBC%20-%20Solution%20NFT%20Puzzle03%20December%202021.py) to the script.

# Puzzle 04

Image 1001.png had some appended bytes at the end of the image. Every file can be identified by the "magic byte/file signature". This is the first few bytes of a file. If you look at the appended bytes, you can see it starts with RIFF or "52 49 46 46" in hex. A file which start with RIFF is a Waveform Audio File Format or better known as a WAV file. When you extract the WAV and play it, you will hear a weird high-pitch noice. The WAV actually contains text. A spectrogram is a visual representation of the spectrum of frequencies of a signal as it varies with time. Spectrograms of audio can be used to identify spoken words phonetically, and to analyse the various calls of animals. A common tool to get the text from a WAV file is Coagula. The text shown is the flag.

:checkered_flag: WBC{WH4T_TH3_W4V}<br>
:link: No script yet.

# Puzzle 05

Image 667.png had some appended bytes at the end of the image. Every file can be identified by the "magic byte/file signature". This is the first few bytes of a file. If you look at the appended bytes, you can see it starts with PK or "50 4B 03 04" in hex. A file which starts with PK is a compressed file. Copying these bytes and change the file extension to .zip will make it easier to extract the file. Unfortunately, the compressed file is password-protected. Since the password can't be found anywhere, you have to brute-force it. I used a common password which can be found in most wordlists. The password to extract the file is "comicbooks". Once extracting the file, the flag is found.

:checkered_flag: WBC{M4Y_TH3_BRUT3_F0RC3_W1TH_Y0U}<br>
:link: [Link](https://github.com/WhiteboardCryptoTeam/Solutions-NFT-Puzzle-December-2021/blob/main/WBC%20-%20Solution%20NFT%20Puzzle05%20December%202021.py) to the script.

# Puzzle 06

This puzzle was the easiest of them all. At image 890.png metadata is added in the 'documentname' field. The data is base64 encoded and can be decoded to get the flag. The base64 encoded string is: V0JDezRMTF9ZMFVSX0I0UzNfNFIzX0IzTDBOR19UMF9VU30= which is WBC{4LL_Y0UR_B4S3_4R3_B3L0NG_T0_US} decoded.

:checkered_flag: WBC{4LL_Y0UR_B4S3_4R3_B3L0NG_T0_US}<br>
:link: No script yet.
