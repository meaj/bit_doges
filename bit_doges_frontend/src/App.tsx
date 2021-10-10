// App.tsx
import ConnectButton from "./components/ConnectButton";
import { ChakraProvider, Heading } from "@chakra-ui/react"
import Layout from "./components/Layout";
import bitdogesGif from './static/BitDoges.gif'

export default function App() {
  return (
    <ChakraProvider>
      <Layout>
        <Heading size="xl" style={{ color: "gold" }}>BitDoges</Heading>
        <img src={bitdogesGif} alt="Rotating BitDoges Logo"/>
        <p style={{ color: "white" }}>hemlo frens</p>
        <ConnectButton />
      </Layout>
    </ChakraProvider>
  )
}
