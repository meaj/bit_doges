// ConnectButton.tsx
import { Button, Box, Text } from "@chakra-ui/react";
import { useEthers, useEtherBalance } from "@usedapp/core";
import { formatEther } from "@ethersproject/units";
import Identicon from "./Identicon";

export default function ConnectButton() {
  const { activateBrowserWallet, account } = useEthers();
  const etherBalance = useEtherBalance(account);
  
  function handleConnectWallet() {
    activateBrowserWallet();
  }
  
  return account ? (
    <Box 
      display="flex"
      alignItems="center"
      background="purple.400"
      borderRadius="xl"
      py="0"
    >
      <Box px="3">       
        <Text color="white" fontSize="md">
          such balance: {etherBalance && parseFloat(formatEther(etherBalance)).toFixed(3)}
        </Text>
      </Box>
      <Button
        bg="purple.800"
        border="1px solid transparent"
        _hover={{
          border:"1px",
          borderStyle: "solid",
          borderColor: "gray.400",
          backgroundColor: "purple:700"
        }}
        borderRadius="xl"
        m="1px"
        px={3}
        height="38px"
      >
        <Text color="white" fontSize="md" fontWeight="medium" mr="2">
          { account && 
              `${account.slice(0,6)}...${account.slice(
              account.length - 4, account.length)}`
          }
        </Text>
        <Identicon />
      </Button>
    </Box>
  ) : (
    <Button onClick={handleConnectWallet}>such connect</Button>
  );
}
