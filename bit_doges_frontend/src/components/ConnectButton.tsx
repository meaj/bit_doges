// ConnectButton.tsx
import { Button, Box, Text } from "@chakra-ui/react";
import { useEthers, useEtherBalance } from "@usedapp/core";

export default function ConnectButton() {
  const { activateBrowserWallet, account } = useEthers();
  const etherBalance = useEtherBalance(account);
  
  function handleConnectWallet() {
    activateBrowserWallet();
  }
  
  return account ? (
    <Box alignItems="center">
      <Text color="white" fontSize="md">
        Balance: {etherBalance && JSON.stringify(etherBalance)} ETH
      </Text>
    </Box>
  ) : (
    <Button onClick={handleConnectWallet}>Connect Wallet</Button>
  );
}
