import { useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import { z } from 'zod'
import { toast } from 'sonner'
import api from '../utils/api'

const contactSchema = z.object({
  name: z.string().min(2, 'Nombre muy corto'),
  email: z.string().email('Email inválido'),
  phone: z.string().optional(),
  subject: z.string().min(3, 'Asunto muy corto'),
  message: z.string().min(10, 'Mensaje muy corto'),
})

export default function ContactForm() {
  const { register, handleSubmit, formState: { errors, isSubmitting }, reset } = useForm({
    resolver: zodResolver(contactSchema),
  })

  const onSubmit = async (data) => {
    try {
      await api.post('/contact', data)
      toast.success('Mensaje enviado correctamente')
      reset()
    } catch {
      toast.error('Error al enviar el mensaje')
    }
  }

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="mx-auto max-w-2xl space-y-4">
      <div className="grid grid-cols-1 gap-4 md:grid-cols-2">
        <div>
          <input {...register('name')} placeholder="Nombre completo" className="input-gaming" />
          {errors.name && <p className="mt-1 text-sm text-red-500">{errors.name.message}</p>}
        </div>
        <div>
          <input {...register('email')} placeholder="Email" className="input-gaming" />
          {errors.email && <p className="mt-1 text-sm text-red-500">{errors.email.message}</p>}
        </div>
      </div>
      <div>
        <input {...register('phone')} placeholder="Teléfono (opcional)" className="input-gaming" />
      </div>
      <div>
        <input {...register('subject')} placeholder="Asunto" className="input-gaming" />
        {errors.subject && <p className="mt-1 text-sm text-red-500">{errors.subject.message}</p>}
      </div>
      <div>
        <textarea
          {...register('message')}
          placeholder="Mensaje"
          rows="5"
          className="input-gaming resize-none"
        />
        {errors.message && <p className="mt-1 text-sm text-red-500">{errors.message.message}</p>}
      </div>
      <div className="text-center">
        <button
          type="submit"
          disabled={isSubmitting}
          className="inline-block rounded-3xl border-8 border-transparent bg-red-500 px-12 py-3 font-black text-white transition hover:border-gray-200 hover:bg-white hover:text-black disabled:cursor-not-allowed disabled:opacity-50"
        >
          {isSubmitting ? 'Enviando...' : 'Enviar Mensaje'}
        </button>
      </div>
    </form>
  )
}
