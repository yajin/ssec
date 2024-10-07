gcc -o vul  -g -fno-pie -no-pie -m32 -fno-stack-protector vul.c
gcc -o vul_aslr  -g -fno-pie -no-pie -m32 -fno-stack-protector vul_aslr.c
