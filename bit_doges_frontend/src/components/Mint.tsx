// Mint.tsx
import {
  Flex,
  Heading,
  Image,
  Stack,
  Text,
} from '@chakra-ui/react';

type Props = {
    mysteryGif: any;
};

export default function MintScreen({ mysteryGif }: Props) {
    return (
    <Stack minH={'100vh'} direction={{ base: 'column', md: 'row' }} bg="purple.800">
      <Flex p={8} flex={1} align={'center'} justify={'center'}>
        <Stack spacing={6} w={'full'} maxW={'lg'}>
        <Heading fontSize={{ base: 'xl', lg: '2xl'}} color={'gold'}>forge a doggy</Heading>
            <Text color={'white'}>🏗 under construction 🚧</Text>
            <Text color={'white'}>minters get to add a doge address to their BitDoge's Metadata (wow)</Text>
        </Stack>
      </Flex>
      <Flex flex={1}>
        <Image
        alt={'Rotating mystery card'}
        objectFit={'cover'}
        src={ mysteryGif }
        />
      </Flex>
    </Stack>
  )
}
