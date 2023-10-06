export default async function Whisp() {
  await new Promise((resolve) => {
    setTimeout(() => {
      resolve(0)
    }, 10000)
  })
  return <div>表示</div>
}
