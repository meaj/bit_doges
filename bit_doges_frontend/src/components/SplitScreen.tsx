import {
  Flex,
  Heading,
  Image,
  Stack,
  Text,
  useBreakpointValue,
} from '@chakra-ui/react';
import AccountModal from "./AccountModal";
import ConnectButton from "./ConnectButton";

type Props = {
    onOpen: any;
    isOpen: any;
    onClose: any;
    dogeGif: any;
};


export default function SplitScreen({ onOpen, isOpen, onClose, dogeGif }: Props) {
    return (
    <Stack minH={'100vh'} direction={{ base: 'column', md: 'row' }} bg="purple.800">
      <Flex p={8} flex={1} align={'center'} justify={'center'}>
        <Stack spacing={6} w={'full'} maxW={'lg'}>
          <Heading fontSize={{ base: '3xl', md: '4xl', lg: '5xl' }}>
            <Text
              as={'span'}
              position={'relative'}
              color={'white'}
              _after={{
                content: "''",
                width: 'full',
                height: useBreakpointValue({ base: '20%', md: '30%' }),
                position: 'absolute',
                bottom: 1,
                left: 0,
                bg: 'yellow.800',
                zIndex: -1,
              }}>
              BitDoges
            </Text>
            <br />{' '}
          </Heading>
          <Text fontSize={{ base: 'md', lg: 'lg' }} color={'white'}>
            Welcome to BitDoges
          </Text>
          <Stack direction={{ base: 'column', md: 'row' }} spacing={4}>
            <ConnectButton handleOpenModal={onOpen} />
            <AccountModal isOpen={isOpen} onClose={onClose} />
          </Stack>
        </Stack>
      </Flex>
      <Flex flex={1}>
        <Image
          alt={'Rotating BitDoges Log'}
          objectFit={'cover'}
          src={ dogeGif }
        />
      </Flex>
    </Stack>
  )
}
