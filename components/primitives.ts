import { tv } from 'tailwind-variants'

export const title = tv({
  base: 'inline font-semibold tracking-tight',
  compoundVariants: [
    {
      class: 'bg-gradient-to-b bg-clip-text text-transparent',
      color: ['violet', 'yellow', 'blue', 'cyan', 'green', 'pink', 'foreground'],
    },
  ],
  defaultVariants: {
    size: 'md',
  },
  variants: {
    color: {
      blue: 'from-[#5EA2EF] to-[#0072F5]',
      cyan: 'from-[#00b7fa] to-[#01cfea]',
      foreground: 'dark:from-[#FFFFFF] dark:to-[#4B4B4B]',
      green: 'from-[#6FEE8D] to-[#17c964]',
      pink: 'from-[#FF72E1] to-[#F54C7A]',
      violet: 'from-[#FF1CF7] to-[#b249f8]',
      yellow: 'from-[#FF705B] to-[#FFB457]',
    },
    fullWidth: {
      true: 'block w-full',
    },
    size: {
      lg: 'text-4xl lg:text-6xl',
      md: 'text-[2.3rem] leading-9 lg:text-5xl',
      sm: 'text-3xl lg:text-4xl',
    },
  },
})

export const subtitle = tv({
  base: 'my-2 block w-full max-w-full text-lg text-default-600 md:w-1/2 lg:text-xl',
  defaultVariants: {
    fullWidth: true,
  },
  variants: {
    fullWidth: {
      true: '!w-full',
    },
  },
})
