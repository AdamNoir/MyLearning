package com.webnoircode.web.app.controllers;

import java.util.ArrayList;
import java.util.List;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import com.webnoircode.web.app.models.Usuario;

@Controller
// Establecer url base
// todas las demas (las de los metodos) deben pasar por esta ruta
@RequestMapping("/app")
public class IndexController {
	
	// Una sola ruta para el controlador
	@GetMapping("/index") // cambiando el verbo cambia el metodo HTTP
	public String index(Model model) { 
		// Objeto de la interfaz model con la que llenar el contenido de la vista(plantilla)
		model.addAttribute("title", "Hola desde Spring - Atributos");
		model.addAttribute("texto", "Yo soy el H1 desde el controlador en Spring");
		return "index";
	}
	
	// Varias rutas en las que se puede llamar el metodo
	@GetMapping({"/home", "/principal", "/inicio"})
	public String inicio(Model model) {
		model.addAttribute("title", "Titulo de la pagina desde varias direcciones");
		model.addAttribute("contenido", "Contenido de la pagina desde varias direcciones");
		return "inicio";
	}
	
	// Vista de Perfil de usuario
	@GetMapping("/perfil")
	public String perfil(Model model) {
		Usuario usuario = new Usuario();
		usuario.setNombre("Ivan");
		usuario.setApellido("Gutierrez");
		model.addAttribute("usuario", usuario);
		model.addAttribute("title", "Perfil: ".concat(usuario.getNombre()));
		return "perfil";
	}
	
	// Vista para Listar
	@GetMapping("/listar")
	public String listar(Model model) {
		List<Usuario> usuarios = new ArrayList<>();
		usuarios.add(new Usuario("Fernando", "Ibarra", "fer@correo.com"));
		usuarios.add(new Usuario("Kenia", "Guerra", "kenia@correo.com"));
		usuarios.add(new Usuario("Suzy", "Cerda", "suzy@correo.com"));
		
		model.addAttribute("title", "Listado de Usuarios");
		model.addAttribute("usuarios", usuarios);
		return "listar";
	}
}
