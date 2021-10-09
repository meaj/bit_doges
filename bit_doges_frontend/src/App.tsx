// App.tsx
import ConnectButton from "./components/ConnectButton";
import { ChakraProvider } from "@chakra-ui/react"
import Layout from "./components/Layout";

export default function App() {
  return (
    <ChakraProvider>
      <Layout>
        <p style={{ color: "white" }}>hemlo frens</p>
        <ConnectButton />
      </Layout>
    </ChakraProvider>
  )
}
