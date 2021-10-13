// NavLink.txs
import { ReactNode } from 'react';
import {
  Box,
  Flex,
  HStack,
  Link,
} from '@chakra-ui/react';
import { Link as RouteLink } from "react-router-dom";
import ConnectButton from './ConnectButton';
import AccountModal from "./AccountModal";

const Links = ['welcome', 'mint', 'roadmap'];

type Props = {
  onOpen: any;
  onClose: any;
  isOpen: any;
};

const NavLink = ({ children }: { children: ReactNode }) => (
  <Link
    px={2}
    py={1}
    rounded={'md'}
    color={'white'}
    _hover={{
      textDecoration: 'none',
      bg: 'purple.700',
    }}
    href={'#'}>
    {children}
  </Link>
);

export default function withAction({ onOpen, isOpen, onClose }: Props) {
  return (
    <Box bg={'purple.900'} px={4}>
    <Flex h={16} alignItems={'center'} justifyContent={'space-between'}>
        <HStack spacing={8} alignItems={'center'}>
        <Box color={'white'}>BitDoges</Box>
        <HStack
            as={'nav'}
            spacing={4}
            display={{ base: 'none', md: 'flex' }}>
            {Links.map((link) => (
              <RouteLink to={link}>
                <NavLink key={link}>{link}</NavLink>
              </RouteLink>
            ))}
        </HStack>
        </HStack>
        <Flex alignItems={'center'}>
        <ConnectButton handleOpenModal={onOpen}/>
	<AccountModal isOpen={isOpen} onClose={onClose} />	
        </Flex>
    </Flex>
    </Box>
  );
}
