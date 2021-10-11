// App.tsx
import { ChakraProvider, useDisclosure } from '@chakra-ui/react';
import theme from './theme';
import SplitScreen from './components/SplitScreen';
import bitdogesGif from './static/BitDoges.gif';
import NavLink from './components/NavLink';
import FooterBar from './components/FooterBar';
import "@fontsource/inter";

export default function App() {
  const { isOpen, onOpen, onClose} = useDisclosure();
  return (
    <ChakraProvider theme={theme}>
      <NavLink onOpen={onOpen} />
      <SplitScreen isOpen={isOpen} onClose={onClose} dogeGif={bitdogesGif} />
      <FooterBar />
    </ChakraProvider>
  )
}
