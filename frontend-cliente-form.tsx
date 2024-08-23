import React, { useState } from 'react';
import { Alert, AlertDescription } from '@/components/ui/alert';

interface ClienteFormData {
  tipo_identificacion: string;
  numero_identificacion: string;
  nombres: string;
  apellidos: string;
  fecha_nacimiento: string;
  direccion: string;
  ciudad: string;
  departamento: string;
  pais: string;
  telefono: string;
  email: string;
}

const ClienteForm: React.FC = () => {
  const [formData, setFormData] = useState<ClienteFormData>({
    tipo_identificacion: '',
    numero_identificacion: '',
    nombres: '',
    apellidos: '',
    fecha_nacimiento: '',
    direccion: '',
    ciudad: '',
    departamento: '',
    pais: '',
    telefono: '',
    email: '',
  });

  const [error, setError] = useState<string | null>(null);

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    setFormData(prevState => ({
      ...prevState,
      [name]: value
    }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await fetch('/api/clientes', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Error al registrar el cliente');
      }
      // Limpiar el formulario después de un registro exitoso
      setFormData({
        tipo_identificacion: '',
        numero_identificacion: '',
        nombres: '',
        apellidos: '',
        fecha_nacimiento: '',
        direccion: '',
        ciudad: '',
        departamento: '',
        pais: '',
        telefono: '',
        email: '',
      });
      setError(null);
    } catch (error) {
      setError(error.message);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <select
        name="tipo_identificacion"
        value={formData.tipo_identificacion}
        onChange={handleInputChange}
        required
        className="w-full p-2 border rounded"
      >
        <option value="">Seleccione tipo de identificación</option>
        <option value="CC">Cédula de Ciudadanía</option>
        <option value="TI">Tarjeta de Identidad</option>
        <option value="CE">Cédula de Extranjería</option>
        <option value="RC">Registro Civil</option>
      </select>
      <input
        type="text"
        name="numero_identificacion"
        value={formData.numero_identificacion}
        onChange={handleInputChange}
        placeholder="Número de Identificación"
        required
        className="w-full p-2 border rounded"
      />
      {/* Agregar campos similares para el resto de los datos del cliente */}
      <button type="submit" className="w-full p-2 bg-blue-500 text-white rounded">
        Registrar Cliente
      </button>
      {error && (
        <Alert variant="destructive">
          <AlertDescription>{error}</AlertDescription>
        </Alert>
      )}
    </form>
  );
};

export default ClienteForm;
