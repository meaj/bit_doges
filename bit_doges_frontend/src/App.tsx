// App.tsx
import { ChakraProvider } from "@chakra-ui/react"
import Layout from "./components/Layout";

export default function App() {
  return (
    <ChakraProvider>
      <Layout>
        <p style={{ color: "white" }}>What's good frens!</p>
      </Layout>
    </ChakraProvider>
  )
}
