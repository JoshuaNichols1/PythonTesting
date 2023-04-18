import {Fragment, useEffect, useRef, useState} from "react"
import {useRouter} from "next/router"
import {E, connect, updateState, uploadFiles} from "/utils/state"
import "focus-visible/dist/focus-visible"
import {Center, CircularProgress, Divider, Heading, Image, Input, VStack, useColorMode} from "@chakra-ui/react"
import NextHead from "next/head"

const PING = "http://localhost:8000/ping"
const EVENT = "ws://localhost:8000/event"
const UPLOAD = "http://localhost:8000/upload"
export default function Component() {
const [state, setState] = useState({"image_made": false, "image_processing": false, "image_url": "", "prompt": "", "events": [{"name": "state.hydrate"}], "files": []})
const [result, setResult] = useState({"state": null, "events": [], "processing": false})
const router = useRouter()
const socket = useRef(null)
const { isReady } = router;
const { colorMode, toggleColorMode } = useColorMode()
const Event = events => setState({
  ...state,
  events: [...state.events, ...events],
})
const File = files => setState({
  ...state,
  files,
})
useEffect(() => {
  if(!isReady) {
    return;
  }
  if (!socket.current) {
    connect(socket, state, setState, result, setResult, router, EVENT, ['websocket', 'polling'])
  }
  const update = async () => {
    if (result.state != null) {
      setState({
        ...result.state,
        events: [...state.events, ...result.events],
      })
      setResult({
        state: null,
        events: [],
        processing: false,
      })
    }
    await updateState(state, setState, result, setResult, router, socket.current)
  }
  update()
})
return (
<Center sx={{"width": "100%", "height": "100vh", "bg": "radial-gradient(circle at 22% 11%,rgba(62, 180, 137,.20),hsla(0,0%,100%,0) 19%)"}}><VStack sx={{"bg": "white", "padding": "2em", "shadow": "lg", "borderRadius": "lg"}}><Heading sx={{"fontSize": "1.5em"}}>{`DALL·E`}</Heading>
<Input onBlur={(_e) => Event([E("state.set_prompt", {value:_e.target.value})])}
placeholder="Enter a prompt.."
type="text"/>
<Divider/>
<Fragment>{state.image_processing ? <Fragment><CircularProgress isIndeterminate={true}/></Fragment> : <Fragment>{state.image_made ? <Fragment><Image src={state.image_url}
sx={{"height": "25em", "width": "25em"}}/></Fragment> : <Fragment/>}</Fragment>}</Fragment></VStack>
<NextHead><title>{`Pynecone:DALL·E`}</title>
<meta content="A Pynecone app."
name="description"/>
<meta content="favicon.ico"
property="og:image"/></NextHead></Center>
)
}