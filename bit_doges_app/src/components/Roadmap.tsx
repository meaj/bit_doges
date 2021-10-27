// Roadmap.tsx
import {
  Flex,
  Heading,
  Image,
  ListItem,
  OrderedList,
  Stack,
} from '@chakra-ui/react';

type Props = {
    dogeGif: any;
};

export default function RoadmapScreen({ dogeGif }: Props) {
    return (
    <Stack minH={'100vh'} direction={{ base: 'column', md: 'row' }} bg="purple.800">
      <Flex p={8} flex={1} align={'center'} justify={'center'}>
        <Stack spacing={6} w={'full'} maxW={'lg'}>
        <Heading fontSize={{ base: 'xl', lg: '2xl'}} color={'gold'}>such plans</Heading>
        <OrderedList fontSize={{ base: 'md', lg: 'lg' }} color={'white'}>
          <ListItem>launch site</ListItem>
          <ListItem>ultra bitdoge giveaways</ListItem>
          <ListItem>minting opens</ListItem>
          <ListItem>???</ListItem>
          <ListItem>we all profit 😎</ListItem>
        </OrderedList>
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
