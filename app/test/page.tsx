'use client'
import { Button } from '@nextui-org/button'
import { Input, Textarea } from '@nextui-org/input'
import { useState, useTransition } from 'react'

import { title } from '@/components/primitives'

import { runCommand } from './action'

export default function Test() {
  const [_, startTransition] = useTransition()
  const [command, setCommand] = useState('')
  const [result, setResult] = useState('')
  return (
    <section className="flex flex-col items-center justify-center gap-4  py-8 md:py-10">
      <div className="inline-block max-w-lg justify-center text-center">
        <h1 className={title()}>コマンドテスト</h1>
      </div>
      <Input
        value={command}
        onChange={(e) => {
          setCommand(e.target.value)
        }}
      />
      <Button
        onClick={(e) => {
          startTransition(async () => {
            const stdout = await runCommand(command)
            setResult(stdout)
          })
        }}
      >
        送信
      </Button>
      <Textarea value={result} readOnly />
    </section>
  )
}
