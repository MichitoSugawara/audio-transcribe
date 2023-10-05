'use server'

import { execSync } from 'child_process'

export async function runCommand(command: string) {
  const stdout = execSync(command)
  return stdout.toString()
}
