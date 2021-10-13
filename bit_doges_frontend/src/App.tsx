// App.tsx
import { ChakraProvider, useDisclosure } from '@chakra-ui/react';
import theme from './theme';
import Welcome from './components/Welcome';
import bitdogesGif from './static/BitDoges.gif';
import NavLink from './components/NavLink';
import FooterBar from './components/FooterBar';
import RoadmapScreen from './components/Roadmap';
import MintScreen from './components/Mint';
import "@fontsource/inter";
import { BrowserRouter as Router, Switch, Route,  } from "react-router-dom";

export default function App() {
  const { isOpen, onOpen, onClose} = useDisclosure();
  return (
    <ChakraProvider theme={theme}>
      <Router>
        <NavLink onOpen={onOpen} isOpen={isOpen} onClose={onClose}/>
        <Switch>
          <Route exact={true} path={["/welcome", "/"]}>
            <Welcome dogeGif={bitdogesGif} />
          </Route>
          <Route path="/roadmap">
            <RoadmapScreen dogeGif={bitdogesGif} />
          </Route>
          <Route path="/mint">
            <MintScreen mysteryGif={bitdogesGif} />
          </Route>
        </Switch>
        <FooterBar />
      </Router>
    </ChakraProvider>
  )
}
