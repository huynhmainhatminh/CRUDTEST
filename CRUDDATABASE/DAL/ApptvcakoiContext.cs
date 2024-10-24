using System;
using System.Collections.Generic;
using Microsoft.EntityFrameworkCore;
using Pomelo.EntityFrameworkCore.MySql.Scaffolding.Internal;

namespace CRUDDATABASE.DAL;

public partial class ApptvcakoiContext : DbContext
{
    public ApptvcakoiContext()
    {
    }

    public ApptvcakoiContext(DbContextOptions<ApptvcakoiContext> options)
        : base(options)
    {
    }

    public virtual DbSet<Product> Products { get; set; }

    public virtual DbSet<ProductType> ProductTypes { get; set; }

    public virtual DbSet<ProductUser> ProductUsers { get; set; }

    public virtual DbSet<QlParameter> QlParameters { get; set; }

    public virtual DbSet<QlUser> QlUsers { get; set; }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder
            .UseCollation("utf8mb4_0900_ai_ci")
            .HasCharSet("utf8mb4");

        modelBuilder.Entity<Product>(entity =>
        {
            entity.HasKey(e => e.Idproduct).HasName("PRIMARY");

            entity
                .ToTable("product")
                .HasCharSet("utf8mb3")
                .UseCollation("utf8mb3_bin");

            entity.HasIndex(e => e.IdproductType, "FK_Idproducttype");

            entity.HasIndex(e => e.Username, "FK_Username");

            entity.Property(e => e.Idproduct).HasColumnName("idproduct");
            entity.Property(e => e.ColorProduct)
                .HasMaxLength(45)
                .HasColumnName("color_product");
            entity.Property(e => e.Description)
                .HasColumnType("text")
                .HasColumnName("description");
            entity.Property(e => e.DestinyProduct)
                .HasMaxLength(45)
                .HasColumnName("destiny_product");
            entity.Property(e => e.IdproductType).HasColumnName("idproduct_type");
            entity.Property(e => e.ImgProduct)
                .HasMaxLength(45)
                .HasColumnName("img_product");
            entity.Property(e => e.NameProduct)
                .HasColumnType("text")
                .HasColumnName("name_product");
            entity.Property(e => e.Username)
                .HasMaxLength(45)
                .HasColumnName("username");

            entity.HasOne(d => d.IdproductTypeNavigation).WithMany(p => p.Products)
                .HasPrincipalKey(p => p.IdproductType)
                .HasForeignKey(d => d.IdproductType)
                .HasConstraintName("FK_Idproducttype");

            entity.HasOne(d => d.UsernameNavigation).WithMany(p => p.Products)
                .HasPrincipalKey(p => p.Username)
                .HasForeignKey(d => d.Username)
                .OnDelete(DeleteBehavior.ClientSetNull)
                .HasConstraintName("FK_Username");
        });

        modelBuilder.Entity<ProductType>(entity =>
        {
            entity.HasKey(e => e.NameType).HasName("PRIMARY");

            entity.ToTable("product_type");

            entity.HasIndex(e => e.IdproductType, "idproduct_type_UNIQUE").IsUnique();

            entity.HasIndex(e => e.NameType, "name_type_UNIQUE").IsUnique();

            entity.Property(e => e.NameType)
                .HasMaxLength(45)
                .HasColumnName("name_type");
            entity.Property(e => e.IdproductType)
                .ValueGeneratedOnAdd()
                .HasColumnName("idproduct_type");
        });

        modelBuilder.Entity<ProductUser>(entity =>
        {
            entity.HasKey(e => e.IdproductUser).HasName("PRIMARY");

            entity
                .ToTable("product_user")
                .HasCharSet("utf8mb3")
                .UseCollation("utf8mb3_bin");

            entity.HasIndex(e => e.IdproductType, "FK_Idproduct_User");

            entity.HasIndex(e => e.Username, "FK_Username_User");

            entity.Property(e => e.IdproductUser).HasColumnName("idproduct_user");
            entity.Property(e => e.ColorProduct)
                .HasMaxLength(45)
                .HasColumnName("color_product")
                .UseCollation("utf8mb4_0900_ai_ci")
                .HasCharSet("utf8mb4");
            entity.Property(e => e.Description)
                .HasColumnType("text")
                .HasColumnName("description")
                .UseCollation("utf8mb4_0900_ai_ci")
                .HasCharSet("utf8mb4");
            entity.Property(e => e.DestinyProduct)
                .HasMaxLength(45)
                .HasColumnName("destiny_product")
                .UseCollation("utf8mb4_0900_ai_ci")
                .HasCharSet("utf8mb4");
            entity.Property(e => e.IdproductType).HasColumnName("idproduct_type");
            entity.Property(e => e.ImgProduct)
                .HasMaxLength(45)
                .HasColumnName("img_product");
            entity.Property(e => e.NameProduct)
                .HasColumnType("text")
                .HasColumnName("name_product")
                .UseCollation("utf8mb4_0900_ai_ci")
                .HasCharSet("utf8mb4");
            entity.Property(e => e.Username)
                .HasMaxLength(45)
                .HasColumnName("username");

            entity.HasOne(d => d.IdproductTypeNavigation).WithMany(p => p.ProductUsers)
                .HasPrincipalKey(p => p.IdproductType)
                .HasForeignKey(d => d.IdproductType)
                .HasConstraintName("FK_Idproduct_User");

            entity.HasOne(d => d.UsernameNavigation).WithMany(p => p.ProductUsers)
                .HasPrincipalKey(p => p.Username)
                .HasForeignKey(d => d.Username)
                .OnDelete(DeleteBehavior.ClientSetNull)
                .HasConstraintName("FK_Username_User");
        });

        modelBuilder.Entity<QlParameter>(entity =>
        {
            entity.HasKey(e => new { e.IdqlParameter, e.NameDestiny })
                .HasName("PRIMARY")
                .HasAnnotation("MySql:IndexPrefixLength", new[] { 0, 0 });

            entity
                .ToTable("ql_parameter")
                .HasCharSet("utf8mb3")
                .UseCollation("utf8mb3_bin");

            entity.HasIndex(e => e.NameDestiny, "name_destiny_UNIQUE").IsUnique();

            entity.Property(e => e.IdqlParameter)
                .ValueGeneratedOnAdd()
                .HasColumnName("idql_parameter");
            entity.Property(e => e.NameDestiny)
                .HasMaxLength(45)
                .HasColumnName("name_destiny")
                .UseCollation("utf8mb4_0900_ai_ci")
                .HasCharSet("utf8mb4");
            entity.Property(e => e.Direction)
                .HasMaxLength(45)
                .HasColumnName("direction")
                .UseCollation("utf8mb4_0900_ai_ci")
                .HasCharSet("utf8mb4");
            entity.Property(e => e.NumberFish)
                .HasMaxLength(45)
                .HasColumnName("number_fish")
                .UseCollation("utf8mb4_0900_ai_ci")
                .HasCharSet("utf8mb4");
        });

        modelBuilder.Entity<QlUser>(entity =>
        {
            entity.HasKey(e => new { e.IdUser, e.Username })
                .HasName("PRIMARY")
                .HasAnnotation("MySql:IndexPrefixLength", new[] { 0, 0 });

            //
			entity.HasKey(e => e.IdUser)
			 .HasName("PRIMARY");

			// Nếu Username cần phải là duy nhất, bạn có thể giữ nguyên ràng buộc uniqueness
			entity.HasIndex(e => e.Username).IsUnique()
				  .HasDatabaseName("username_UNIQUE");

			entity
                .ToTable("ql_user")
                .HasCharSet("utf8mb3")
                .UseCollation("utf8mb3_bin");

            entity.HasIndex(e => e.Username, "username_UNIQUE").IsUnique();

            entity.Property(e => e.IdUser)
                .ValueGeneratedOnAdd()
                .HasColumnName("id_user");
            entity.Property(e => e.Username)
                .HasMaxLength(45)
                .HasColumnName("username");
            entity.Property(e => e.AccessUser)
                .HasMaxLength(10)
                .HasDefaultValueSql("'user'")
                .HasColumnName("access_user");
            entity.Property(e => e.Email)
                .HasMaxLength(45)
                .HasColumnName("email");
            entity.Property(e => e.Facebook)
                .HasColumnType("text")
                .HasColumnName("facebook");
            entity.Property(e => e.NameUser)
                .HasMaxLength(45)
                .HasColumnName("name_user");
            entity.Property(e => e.PassUser)
                .HasMaxLength(45)
                .HasColumnName("pass_user");
            entity.Property(e => e.Phone)
                .HasMaxLength(45)
                .HasColumnName("phone");
        });

        OnModelCreatingPartial(modelBuilder);
    }

    partial void OnModelCreatingPartial(ModelBuilder modelBuilder);
}
