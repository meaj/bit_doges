import {
  Flex,
  Heading,
  Image,
  Stack,
  Text,
} from '@chakra-ui/react';
import AccountModal from "./AccountModal";

type Props = {
    isOpen: any;
    onClose: any;
    dogeGif: any;
};


export default function SplitScreen({ isOpen, onClose, dogeGif }: Props) {
    return (
    <Stack minH={'100vh'} direction={{ base: 'column', md: 'row' }} bg="purple.800">
      <Flex p={8} flex={1} align={'center'} justify={'center'}>
        <Stack spacing={6} w={'full'} maxW={'lg'}>
          <Heading fontSize={{ base: '3xl', md: '4xl', lg: '5xl' }}>
            <Text
              as={'span'}
              position={'relative'}
              color={'white'}
              >
              BitDoges
            </Text>
          </Heading>
          <Text fontSize={{ base: 'md', lg: 'lg' }} color={'white'}>
            hemlo, welcome to the party
          </Text>
          <Stack direction={{ base: 'column', md: 'row' }} spacing={4}>
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
