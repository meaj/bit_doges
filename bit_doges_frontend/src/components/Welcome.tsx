// Welcome.tsx
import {
  Flex,
  Heading,
  Image,
  Stack,
  Text,
} from '@chakra-ui/react';

type Props = {
    dogeGif: any;
};

export default function Welcome({ dogeGif }: Props) {
    return (
    <Stack minH={'100vh'} direction={{ base: 'column', md: 'row' }} bg="purple.800">
      <Flex p={8} flex={1} align={'center'} justify={'center'}>
        <Stack spacing={6} w={'full'} maxW={'lg'}>
        <Heading fontSize={{ base: '2xl', lg: '3xl'}} color={'gold'}>oh, hai</Heading>	
        <Text fontSize={{ base: 'md', lg: 'lg' }} color={'white'}>
          hemlo, welcome to the party
        </Text>
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
