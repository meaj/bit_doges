// App.tsx
import ConnectButton from "./components/ConnectButton";
import { ChakraProvider, Heading, useDisclosure } from "@chakra-ui/react";
import theme from "./theme";
import Layout from "./components/Layout";
import AccountModal from "./components/AccountModal";
import bitdogesGif from './static/BitDoges.gif';
import "@fontsource/inter";

export default function App() {
  const { isOpen, onOpen, onClose} = useDisclosure();
  return (
    <ChakraProvider theme={theme}>
      <Layout>
        <Heading size="xl" style={{ color: "gold" }}>BitDoges</Heading>
        <img src={bitdogesGif} alt="Rotating BitDoges Logo"/>
        <p style={{ color: "white" }}>hemlo frens</p>
        <ConnectButton handleOpenModal={onOpen} />
        <AccountModal isOpen={isOpen} onClose={onClose} />
      </Layout>
    </ChakraProvider>
  )
}
